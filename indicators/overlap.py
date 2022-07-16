from base import OHLCV


class OverlapStudies(OHLCV):

    def __init__(self, open_: list, high_: list, low_: list, close_: list, volume_: list) -> None:
        """Initializes the class accessing properties of the parent class OHLCV"""

        super().__init__(open_, high_, low_, close_, volume_)

    def bbands(self, source: list, length: int = 20, multiplier: int = 2):
        sd = []

        for x in range(len(source) + 1):
            if x >= length:
                middle_band = round(sum(source[x-length:x]) / length, 6)
                sample_price = source[x-length:x]

                for y in range(length):
                    sd.append(round((sample_price[y] - middle_band) ** 2, 6))

                st_dev = round((sum(sd) / length) ** (1/2), 6)
                sd.clear()
                upper_band = middle_band + (st_dev * multiplier)
                lower_band = middle_band - (st_dev * multiplier)

        return upper_band, middle_band, lower_band

    def ema(self, source: list, length: int = 10):
        """The exponential moving average (EMA) is a type of moving average (MA) that 
        places a greater weight and significance on the most recent data points.
        See https://www.investopedia.com/terms/e/ema.asp
        
        Function Args:
        source: Data Array
        length(default) = 14"""

        smoothing_constant = 2 / (length + 1)
        ema_array = []

        # runs a loop for x times where x is the length of the sample data.
        for x in range(len(source)):
            if x == 0:
                # calculates smoothed moving average of source of the starting length values
                _sma = sum(source[:length]) / length

            if x == 1:
                _ema = (source[x] - _sma) * smoothing_constant + _sma
                ema_array.append(round(_ema, 2))
 
            if x > 1:
                _ema = (source[x] - ema_array[-1]) * smoothing_constant + ema_array[-1]
                ema_array.append(round(_ema, 2))

        return ema_array

    def psar(self, start: int = 0.02, inc: int = 0.02, maximum: int = 0.2):
        """The parabolic SAR indicator is used by traders to determine trend direction and 
        potential reversals in price. The indicator uses a trailing stop and reverse method 
        called "SAR," or stop and reverse, to identify suitable exit and entry points.
        See https://www.investopedia.com/terms/p/parabolicindicator.asp"""
        
        sar_array = []

        for x in range(1, len(self.close)):
            if x == 1:
                if self.close[x] > self.close[x-1]:
                    is_below = True
                    max_min = self.high[x]
                    sar = self.low[x-1]
                else:
                    is_below = False
                    max_min = self.low[x]
                    sar = self.high[x-1]
                acceleration = start

            sar = sar + acceleration * (max_min - sar)

            if is_below:
                if sar > self.low[x]:
                    is_below = False
                    sar = max(self.high[x], max_min)
                    max_min = self.low[x]
                    acceleration = start
            else:
                if sar < self.high[x]:
                    is_below = True
                    sar = min(self.low[x], max_min)
                    max_min = self.high[x]
                    acceleration = start

            if is_below:
                if self.high[x] > max_min:
                    max_min = self.high[x]
                    acceleration = min(acceleration + inc, maximum)
                sar = min(sar, self.low[x-1])
                if x > 1:
                    sar = min(sar, self.low[x-2])

            else:
                if self.low[x] < max_min:
                    max_min = self.low[x]
                    acceleration = min(acceleration + inc, maximum)
                sar = max(sar, self.high[x-1])
                if x > 1:
                    sar = max(sar, self.high[x-2])

            sar_array.append(round(sar, 2))

        return sar_array

    def rma(self, source: list, length: int = 10):
        rma_array = []
        alpha = 1 / length

        for x in range(len(source)):

            if x == length:
                rma_array.append(sum(source[x-length:x]) / length)

            elif x >= length:
                rma_array.append(
                    alpha * source[x] + (1 - alpha) * rma_array[-1])

        return rma_array

    def sma(self, source: list, length: int = 10):
        sma_array = []

        for x in range(len(source)):
            if x >= length:
                sma_array.append(sum(source[x-length:x]) / length)

        return sma_array

    def vwap(self, length: int = 14):
        tpxv_array = []
        vwap_array = []

        for x in range(len(self.volume) + 1):
            if x < len(self.volume):
                tp = (self.high[x] + self.low[x] + self.close[x]) / 3
                tpxv = tp * self.volume[x]
                tpxv_array.append(tpxv)

            if x >= length:
                vwap_array.append(
                    sum(tpxv_array[x-length:x]) / sum(self.volume[x-length:x]))

        return vwap_array

    def wma(self, source: list, length: int = 10):
        weighted_array = []
        wma_array = []

        for x in reversed(range(length)):
            weighted_array.append(x + 1)

        for x in range(len(source) + 1):
            if x >= length:
                sample_array = source[x-length:x][::-1]
                element_wise_multiplication = [
                    a * b for a, b in zip(sample_array, weighted_array)]
                result = sum(element_wise_multiplication) / sum(weighted_array)
                wma_array.append(round(result, 2))

        return wma_array

from base import OHLCV
from overlap import OverlapStudies


class MomentumIndicators(OHLCV):
    """Momentrum indicators are technical analysis tools used to determine the 
    strength or weakness of a stock's price. Momentum measures the rate of the 
    rise or fall of asset prices."""

    def __init__(self, open_: list, high_: list, low_: list, close_: list, volume_: list) -> None:
        """Initializes the class accessing properties of the parent class OHLCV"""

        super().__init__(open_, high_, low_, close_, volume_)

    def cci(self, length: int = 20):
        """The Commodity Channel Index (CCI) is a technical indicator that 
        measures the difference between the current price and the historical
        average price.
        See https://www.investopedia.com/terms/c/commoditychannelindex.asp

        Function Args:
        length(default) = 14"""

        tp_array = [None for x in range(len(self.close))] # list comprehension that creates an array of length(close) with each element as 'None'
        sma_array = []
        abs_values = []
        cci_array = []

        for x in range(len(self.close) + 1):
            if x < len(self.close):
                tp_array[x] = round((self.high[x] + self.low[x] + self.close[x]) / 3, 2) # tp: typical price

            if x >= length:
                sma_array.append(round(sum(tp_array[x-length:x]) / length, 2))
                sample_tp_array = tp_array[x-length:x]

                for y in range(length):
                    _ = abs(sample_tp_array[y] - sma_array[-1])
                    abs_values.append(_)

                mean_deviation = round(sum(abs_values) / length, 2)
                abs_values.clear()
                # subtracts the element of tp_array which matches the element that of sma_array
                # since sma_array is formed after x >= length the latest element of sma_array will
                # not be equal to the recent element of tp_array, hence the indexing is done by x-1
                cci_array.append(round((tp_array[x-1] - sma_array[-1]) / (0.015 * mean_deviation), 2))

        return cci_array

    def dmi(self, length: int = 14):
        """The directional movement index (DMI) is an indicator that identifies 
        in which direction the price of an asset is moving. It also gauges the
        strength of the uptrend or downtrend.
        See https://www.investopedia.com/terms/d/dmi.asp

        Function Args:
        length(default) = 14"""

        tr_array = []
        plus_dm_array = []
        minus_dm_array = []
        _adx = []
        plus_di_array = []
        minus_di_array = []
        adx_array = []

        for x in range(len(self.high)):
            if x == 0:
                tr_array.append(round(self.high[x] - self.low[x], 4))

            elif x > 0:
                tr_array.append(max([round(self.high[x] - self.low[x], 2), round(abs(
                    self.high[x] - self.close[x-1]), 2), round(abs(self.low[x] - self.close[x-1]), 4)]))
                up = self.high[x] - self.high[x-1]
                down = (self.low[x] - self.low[x-1]) * -1

                if up > down and up > 0:
                    plus_dm = up
                else:
                    plus_dm = 0

                if down > up and down > 0:
                    minus_dm = down
                else:
                    minus_dm = 0

                plus_dm_array.append(plus_dm)
                minus_dm_array.append(minus_dm)

                if len(tr_array) >= length:
                    tr_rma = OverlapStudies.rma(tr_array, length)

                    if tr_rma:
                        # try except clause is used as the rma function returns an empty array uptil x == length
                        # as the last element cannot be mathematically operated hence the try and except clause is
                        # used, refer to OverlapStudies.rma
                        try:
                            plus_di = (100 * OverlapStudies.rma(plus_dm_array, length)[-1] / tr_rma[-1])
                            minus_di = (100 * OverlapStudies.rma(minus_dm_array, length)[-1] / tr_rma[-1])
                            plus_di_array.append(round(plus_di, 4))
                            minus_di_array.append(round(minus_di, 4))
                            addition = plus_di + minus_di

                            if addition == 0:
                                addition = 1

                            _adx.append(abs(plus_di - minus_di) / addition)
                            adx_array.append(round(100 * OverlapStudies.rma(_adx, length)[-1], 4))
                        except:
                            pass

        return adx_array, plus_di_array, minus_di_array

    def macd(self, fast_length: int = 12, slow_length: int = 26, signal_length: int = 9):
        """Moving average convergence divergence (MACD) is a trend-following 
        momentum indicator that shows the relationship between two moving 
        averages of an asset's price
        See https://www.investopedia.com/terms/m/macd.asp
        
        Function Args:
        fast_length(default) = 12; period lenth for moving average
        slow_length(default) = 26; period lenth for moving average
        signal_length(default) = 9; period lenth for moving average"""

        ema12 = OverlapStudies.ema(self.close, fast_length)
        ema26 = OverlapStudies.ema(self.close, slow_length)

        macd_array = [None for x in range(len(ema26))] # list comprehension that creates an array of length(ema26) with each element as 'None'

        for x in range(len(ema26)):
            macd_array[x] = round(ema12[x] - ema26[x], 2)

        macd_signal_array = OverlapStudies.ema(macd_array, signal_length)
        macd_signal_array.insert(0, 0)

        macd_histogram_array = [None for x in range(len(macd_array))]

        for x in range(len(macd_array)):
            macd_histogram_array[x] = round(
                macd_array[x] - macd_signal_array[x], 2)

        return macd_array, macd_signal_array, macd_histogram_array

    def rsi(self, length: int = 14):
        """The relative strength index (RSI) is a momentum indicator which 
        measures the speed and magnitude of an asset's recent price 
        changes to evaluate overvalued or undervalued conditions in the 
        price of that asset.
        See https://www.investopedia.com/terms/r/rsi.asp

        Function Args:
        length(default) = 14"""

        change = [0 for x in range(len(self.close) - 1)]
        gain = [0 for x in range(len(self.close) - 1)]
        loss = [0 for x in range(len(self.close) - 1)]
        average_gain = []
        average_loss = []
        rsi_array = []

        for x in range(len(self.close) - 1):
            if x > 0:
                change[x] = round(self.close[x+1] - self.close[x], 2)
                if change[x] > 0:
                    gain[x] = change[x]
                    loss[x] = 0
                elif change[x] < 0:
                    loss[x] = abs(change[x])
                    gain[x] = 0

            if x == length:
                _gain = sum(gain[:length+1]) / length
                _loss = sum(loss[:length+1]) / length
                average_gain.append(round(_gain, 2))
                average_loss.append(round(_loss, 2))
                rs = average_gain[-1] / average_loss[-1]
                rsi_array.append(round(100 - (100 / (1 + rs)), 2))

            if x > length:
                _gain = ((average_gain[-1] * (length - 1)) + gain[x]) / length
                _loss = ((average_loss[-1] * (length - 1)) + loss[x]) / length
                average_gain.append(round(_gain, 2))
                average_loss.append(round(_loss, 2))
                rs = average_gain[-1] / average_loss[-1]
                rsi_array.append(round(100 - (100 / (1 + rs)), 2))

        return rsi_array

    def stoch(self, length: int = 14, smooth_d: int = 14):
        """A stochastic oscillator is a momentum indicator comparing 
        a particular closing price of a security to a range of its 
        prices over a certain period of time.
        See https://www.investopedia.com/terms/s/stochasticoscillator.asp

        Function Args:
        length(default) = 14
        smooth_d(default) = 14"""
        
        k = []
        d = []

        for x in range(len(self.high)):
            if x >= length:
                k.append(((self.close[x] - min(self.low[x-length:x])) /
                          (max(self.high[x-length:x]) - min(self.low[x-length:x]))) * 100)

        for x in range(len(k) + 1):
            if x >= smooth_d:
                print(len(k[x-3:x]))
                d.append(sum(k[x-3:x]) / 3)

        return k, d

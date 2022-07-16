from base import OHLCV


class VolatilityIndicators(OHLCV):
    """The volatility indicator is a technical tool that measures how far security
    stretches away from its mean price, higher and lower. It computes the dispersion 
    of returns over time in a visual format that technicians use to gauge whether 
    this mathematical input is increasing or decreasing."""

    def __init__(self, open_: list, high_: list, low_: list, close_: list, volume_: list) -> None:
        """Initializes the class accessing properties of the parent class OHLCV"""

        super().__init__(open_, high_, low_, close_, volume_)

    def atr(self, length: int = 14) -> list:
        """The average true range (ATR) is a market volatility indicator used in technical 
        analysis. It is typically derived from the 14-day simple moving average of a series
        of true range indicators. The ATR was originally developed for use in commodities
        markets but has since been applied to all types of securities.
        See https://www.investopedia.com/terms/a/atr.asp

        Function Args:
        length(default) = 14"""

        tr_array = []
        atr_array = []

        # runs a loop for x times where x is the length of the sample data.
        for x in range(len(self.close)):
            if x == 0:
                # subracts the value of low from high at current index and rounds the value before appending them to tr_array
                tr_array.append(round(self.high[x] - self.low[x], 2))

            elif x > 0:
                # subracts the value of low from high at current index
                # subracts the value of close of the previous index from high at current index and takes the absolute of the result
                # subracts the value of close of the previous index from low at current index and takes the absolute of the result
                # then appends the rounded maximum value to tr_array
                tr_array.append(round(max([self.high[x] - self.low[x], abs(
                    self.high[x] - self.close[x-1]), abs(self.low[x] - self.close[x-1])]), 2))

            if x == length:
                # takes the rounded moving average of true range of "length" values at a time and appends the value to atr_array
                atr_array.append(round(sum(tr_array[x-length:x]) / length, 2))

            elif x > length:
                _atr = ((atr_array[-1] * (length - 1)) + tr_array[-1]) / length
                atr_array.append(round(_atr, 2))

        return atr_array

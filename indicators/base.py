class OHLCV:

    def __init__(self, open_: list, high_: list, low_: list, close_: list, volume_: list) -> None:

        """Initializes the class. Args include, OHLCV data from candlesticks as individual arrays.
        OHLCV data includes open, high, low, close values from a candlestick chart and volume at 
        each interval, where the open and close represent the first and the last price level during
        a specified interval. high and low represent the highest and lowest reached price during 
        that interval.
        See - https://www.kaiko.com/collections/ohlcv"""

        self.open = open_
        self.high = high_
        self.low = low_
        self.close = close_
        self.volume = volume_
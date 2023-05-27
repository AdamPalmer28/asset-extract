"""
Class for extracting stock data from yahoo finance

"""

from .asset_base import AssetData

import pandas as pd


class StockData(AssetData):

    def __init__(self):
        
        super().__init__()

#1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
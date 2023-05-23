"""
Class for extracting stock data from yahoo finance

"""

from .asset_cl import AssetData

import pandas as pd


class StockData(AssetData):

    def __init__(self):
        
        super().__init__()


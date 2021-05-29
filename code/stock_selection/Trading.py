from Investment.Trading.TradingBase import TradingBase
from datetime import date


class Trading(TradingBase):
    def __init__(self):
        super().__init__

    def __repr__(self):
        return self.Name

    def setTrading(self):
        super().setTrading()
        self.Name = 'Split evenly'
        self.TotalInvestmentAmount = 100000000
        self.Method = 1  # 1 : "Split evenly",
        self.BuyingMethod = 1  # 1 : at once 
        self.BuyingDateTime.append(date(2017, 4, 10))
        self.SellDateTime.append(date(2017, 7, 10))
        self.NumberOfStocks = 10
        self.PriceDiv = 'Open'
        self.StockBuyingSearchTarget.append('Open')
        self.StockSellSearchTarget.append('Open')

    def doTrading(self):
        return super().doTrading()

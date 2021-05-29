import pandas as pd

class TradingBase:
    Name = ''
    TotalInvestmentAmount = 0
    Method = "Split evenly" 
    BuyingMethod = 1 # 1 : at_once 
    BuyingDateTime = [] # datetime
    SellDateTime = [] # datetime
    NumberOfStocks = 10
    PriceDiv = "Open"
    StockBuyingSearchTarget = []
    StockSellSearchTarget = []

    df_all = None
    df_stock = None
    db = None

    def __init__(self):
        self.Name = 'Base'

    def __repr__(self):
        return self.Name

    def setTrading(self):
        print("setTrading")

    def doTrading(self):
        self.df_all['BuyingPrice'] = 0   
        self.df_all['SellPrice'] = 0   
        self.df_all['BuyingAmount'] = 0   

        if self.Method == 1: # "Split evenly"
            if self.BuyingMethod == 1:
                investmentAmount = self.TotalInvestmentAmount / self.NumberOfStocks
                for index, row in self.df_all.iterrows():
                    self.df_stock = self.db.findSPbyID(self.StockBuyingSearchTarget, self.df_all.loc[index, 'StockCode'], self.BuyingDateTime[0].strftime("%Y-%m-%d")) 
                    if self.df_stock is None :
                        print('db query error')
                    else:
                        if self.df_stock.size < 1 :
                            continue
                    buyingPrice = self.df_stock[self.StockBuyingSearchTarget[0]][0]

                    self.df_stock = self.db.findSPbyID(self.StockSellSearchTarget, self.df_all.loc[index, 'StockCode'], self.SellDateTime[0].strftime("%Y-%m-%d")) 
                    if self.df_stock is None :
                        print('db query error')
                    else:
                        if self.df_stock.size < 1 :
                            continue
                    sellPrice = self.df_stock[self.StockSellSearchTarget[0]][0]
                    
                    self.df_all.loc[index, 'BuyingPrice'] = buyingPrice  
                    self.df_all.loc[index, 'SellPrice'] = sellPrice  
                    self.df_all.loc[index, 'BuyingAmount'] = int(investmentAmount / buyingPrice)

            elif self.BuyingMethod == 2:
                print('...')    
            else:
                print('...')
        else:
            print('...')          
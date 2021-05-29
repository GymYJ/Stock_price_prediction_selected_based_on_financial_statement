from datetime import date
import pandas as pd
import sys 
from Investment.Strategy.StrategyBase import StrategyBase

class FinancialStatementsStrategyBase(StrategyBase):
    AdditionalFinancialStatementsItem = []
    FinancialStatementsCondition = ''
    FinancialStatementsYear = 2017
    FinancialStatementsQuater = 1
    FinancialStatementsDiv = 'CFS'
    StockDate = date.today()
    DataSearchStartDate = date.today()
    DataSearchEndDate = date.today()
    FinancialStatementsSearchTarget = []
    StockSearchTarget = []
    FinancialStatementsOrderBy = []
    FinancialStatementsOrderMethod = ''
    
    df_fs = None
    df_stock = None
    df_company = None

    def __init__(self):
        super().__init__ 
        self.Division = "FinancialStatements"

    def __repr__(self):
        return self.Name

    def setStrategy(self):
        super().setStrategy()

    def searchData(self):
        try:
            self.df_fs = self.db.findFS(self.FinancialStatementsSearchTarget, self.FinancialStatementsYear, self.FinancialStatementsQuater, self.FinancialStatementsDiv)
            if( self.df_fs is None) :
                print('db query error')
                sys.exit(1)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            return False
        return True

    def setAdditionalData(self):
        try:
            for item in self.AdditionalFinancialStatementsItem: 
                self.df_fs[item] = 0

                for item in self.StockSearchTarget: 
                    self.df_fs[item] = 0

                for index, row in self.df_fs.iterrows():
                    self.df_stock = self.db.findSPbyID(self.StockSearchTarget, row['StockCode'], self.StockDate.strftime("%Y-%m-%d")) 
                    if self.df_stock is None :
                        print('db query error')
                    else :
                        if self.df_stock.size < 1 :
                            continue
                        for item in self.StockSearchTarget: 
                            self.df_fs.loc[index, item] = self.df_stock[item][0]
                        
                        for item in self.AdditionalFinancialStatementsItem:
                            if item == 'PER':
                                if row["ProfitLoss"] != 0 :
                                    self.df_fs.loc[index, item] = self.df_fs.loc[index, 'MarketCapitalization']/row["ProfitLoss"]
                            elif item == 'PBR':
                                if row["Equity"] != 0 :
                                    self.df_fs.loc[index, item] = self.df_fs.loc[index, 'MarketCapitalization']/row["Equity"]
                            elif item == 'ROE':
                                if row["Equity"] != 0 :
                                    self.df_fs.loc[index, item] = float(row["ProfitLoss"])/float(row["Equity"]) * 100.00
                            elif item == 'PSR':
                                if row["Revenue"] != 0 :
                                    self.df_fs.loc[index, item] = self.df_fs.loc[index, 'MarketCapitalization']/row["Revenue"]
                            elif item == 'PCR':
                                if row["CashAndCashEquivalentsAtEndOfPeriodCf"] != 0 :
                                    self.df_fs.loc[index, item] = self.df_fs.loc[index, 'MarketCapitalization']/row["CashAndCashEquivalentsAtEndOfPeriodCf"]
                            elif item == 'DR':
                                if row["Equity"] != 0 :
                                    self.df_fs.loc[index, item] = float(row["Liabilities"])/float(row["Equity"]) * 100.00
                            elif item == 'OM':
                                if row["Revenue"] != 0 :
                                    self.df_fs.loc[index, item] = float(row["OperatingIncomeLoss"])/float(row["Revenue"]) * 100.00
                            elif item == 'NPM':
                                if row["Revenue"] != 0 :
                                    self.df_fs.loc[index, item] = float(row["ProfitLoss"])/float(row["Revenue"]) * 100.00
                asc = True
                if self.FinancialStatementsOrderMethod == 'asc':
                    asc = True
                elif self.FinancialStatementsOrderMethod == 'desc':
                    asc = False
                self.df_all = self.df_fs.query(self.FinancialStatementsCondition).sort_values(by=self.FinancialStatementsOrderBy, ascending=asc).head(self.NumberOfStocks)
                self.df_all.insert(1,'StockName','')
                self.df_all['StockName'] = ''

                for index, row in self.df_all.iterrows():
                    self.df_all.loc[index, "StockName"] = self.db.findStockName(row['StockCode'])

        except:
            print("Unexpected error:", sys.exc_info()[0])
            return False
        return True
    
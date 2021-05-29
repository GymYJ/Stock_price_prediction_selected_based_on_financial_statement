from Investment.Strategy.FinancialStatementsStrategyBase import FinancialStatementsStrategyBase
from datetime import date


class Strategy(FinancialStatementsStrategyBase):
    def __init__(self):
        super().__init__

    def __repr__(self):
        return self.Name

    def setStrategy(self):
        super().setStrategy()
        self.Name = 'PER_ROE_V1.0'
        self.NumberOfStocks = 10
        self.AdditionalFinancialStatementsItem.append('PER')
        self.AdditionalFinancialStatementsItem.append('PBR')
        self.AdditionalFinancialStatementsItem.append('ROE')
        self.FinancialStatementsCondition = '(PER > 0) and (PBR < 0.7) and (ROE > 11)'
        self.FinancialStatementsYear = 2016
        self.FinancialStatementsQuater = 4
        self.FinancialStatementsDiv = 'CFS'
        self.StockDate = date(2017, 4, 10)
        self.FinancialStatementsSearchTarget.append('StockCode')
        self.FinancialStatementsSearchTarget.append('Equity')
        self.FinancialStatementsSearchTarget.append('ProfitLoss')
        self.FinancialStatementsSearchTarget.append('CashAndCashEquivalentsAtEndOfPeriodCf')
        self.FinancialStatementsSearchTarget.append('Revenue')
        self.StockSearchTarget.append('MarketCapitalization')
        self.FinancialStatementsOrderBy.append('PER')
        self.FinancialStatementsOrderMethod = 'asc'

    def searchData(self):
        return FinancialStatementsStrategyBase.searchData(self)

    def setAdditionalData(self):
        return FinancialStatementsStrategyBase.setAdditionalData(self)

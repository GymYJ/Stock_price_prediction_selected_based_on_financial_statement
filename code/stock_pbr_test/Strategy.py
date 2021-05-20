from Investment.Strategy.StrategyBase import StrategyBase
from Investment.Strategy.FinancialStatementsStrategyBase import FinancialStatementsStrategyBase
from datetime import date


class Strategy(FinancialStatementsStrategyBase):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return self.Name

    def setStrategy(self, per=None, pbr_up=None, pbr_down=None, roe=None, order='PER'):
        super().setStrategy()
        self.Name = 'PER_ROE_V1.0'
        self.NumberOfStocks = 10
        self.AdditionalFinancialStatementsItem = ['PER', 'PBR', 'ROE']
        # self.FinancialStatementsCondition = '(PER > 6) and (ROE > 10) and (PBR > 0.5) and (PBR < 1)'
        self.setFinancialStatementsCondition(per, pbr_up, pbr_down, roe)
        print(self.FinancialStatementsCondition)
        # self.FinancialStatementsCondition = '(PER > 0) and (PER < 20) and (ROE > 10)'
        # self.FinancialStatementsCondition = '(PBR < 1)'
        self.FinancialStatementsYear = 2016
        self.FinancialStatementsQuater = 4
        self.FinancialStatementsDiv = 'CFS'
        self.StockDate = date(2017, 4, 10)
        self.FinancialStatementsSearchTarget = ['StockCode', 'Equity', 'ProfitLoss']
        self.StockSearchTarget = ['MarketCapitalization']
        self.FinancialStatementsOrderBy = [order]
        if order == 'PER':
            self.FinancialStatementsOrderMethod = 'asc'
        else:
            self.FinancialStatementsOrderMethod = 'desc'
        # self.FinancialStatementsOrderBy.append('ROE')
        # self.FinancialStatementsOrderMethod = 'desc'

    def setFinancialStatementsCondition(self, per, pbr_up, pbr_down, roe):
        self.FinancialStatementsCondition = ''
        if per is not None:
            self.FinancialStatementsCondition += f'(PER > {per})'
        if pbr_up:
            if len(self.FinancialStatementsCondition) == 0:
                self.FinancialStatementsCondition += f'(PBR > {pbr_up})'
            else:
                self.FinancialStatementsCondition += f' and (PBR > {pbr_up})'
        if pbr_down:
            if len(self.FinancialStatementsCondition) == 0:
                self.FinancialStatementsCondition += f'(PBR < {pbr_down})'
            else:
                self.FinancialStatementsCondition += f' and (PBR < {pbr_down})'
        if roe:
            if len(self.FinancialStatementsCondition) == 0:
                self.FinancialStatementsCondition += f'(ROE > {roe})'
            else:
                self.FinancialStatementsCondition += f' and (ROE > {roe})'

    def searchData(self):
        return FinancialStatementsStrategyBase.searchData(self)

    def setAdditionalData(self):
        return FinancialStatementsStrategyBase.setAdditionalData(self)

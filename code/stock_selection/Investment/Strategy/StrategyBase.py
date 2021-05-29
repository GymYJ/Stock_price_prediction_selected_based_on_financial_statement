from datetime import date

class StrategyBase:
    Name = ''
    Division = ''
    NumberOfStocks = 0    
    DataSearchStartDate = date.today()
    DataSearchEndDate = date.today()
    
    df_all = None
    db  = None

    def __init__(self):
        self.Name = 'Base'        

    def __repr__(self):
        return self.Name

    def setStrategy(self):
        print('setStrategy')        

    def searchData(self):
        print('searchData')

    def setAdditionalData(self):
        print('setAdditionalData')
    
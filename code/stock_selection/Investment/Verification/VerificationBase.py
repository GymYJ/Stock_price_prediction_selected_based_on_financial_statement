import pandas as pd
import json

class VerificationBase:
    Name = ''
    TotalInvestmentAmount = 0
    Balance: int = 0
    Yield: float = 0
    
    df_all = None # type: pd
    db = None

    def __init__(self):
        self.Name = 'Base'

    def __repr__(self):
        return self.Name

    def setVerification(self):
        print("setVerification")

    def doVerification(self):
        self.df_all['ProfitLossByStock'] = 0   
        self.df_all['InvestmentAmount'] = 0   
        self.df_all['Balance'] = 0   
        self.df_all['Yield'] = 0  

        for index, row in self.df_all.iterrows():
            buyingPrice = self.df_all.loc[index, 'BuyingPrice']
            sellPrice = self.df_all.loc[index, 'SellPrice']
            investmentCurrentAmount = self.df_all.loc[index, 'BuyingAmount'] * buyingPrice
            self.df_all.loc[index, 'ProfitLossByStock'] = sellPrice - buyingPrice
            self.df_all.loc[index, 'InvestmentAmount'] = investmentCurrentAmount
            self.df_all.loc[index, 'Balance'] = investmentCurrentAmount + self.df_all.loc[index, 'ProfitLossByStock'] * self.df_all.loc[index, 'BuyingAmount']
            self.df_all.loc[index, 'Yield'] = (float(self.df_all.loc[index, 'Balance']) - float(investmentCurrentAmount))/float(investmentCurrentAmount) * 100.00
                
        self.Balance = self.df_all['Balance'].sum()
        investmentCurrentTotalAmount = self.df_all['InvestmentAmount'].sum()
        self.df_all = self.df_all.append(pd.Series(), ignore_index = True)
        self.df_all.loc[len(self.df_all)-1, 'Balance'] = self.Balance
        self.Yield = ((float(self.Balance) + float(self.TotalInvestmentAmount - investmentCurrentTotalAmount)) - float(self.TotalInvestmentAmount))/float(self.TotalInvestmentAmount) * 100.00      
        self.df_all.loc[len(self.df_all)-1, 'Yield'] = self.Yield

    def saveResult(self):
        self.df_all.to_csv("result.csv")
        self.df_all.to_csv("result_kr.csv", encoding='euc-kr')

    def saveResulToJSON(self):
        result = self.df_all.to_json(orient="split")
        parsed = json.loads(result)
        with open("result.json", "w") as text_file:
            text_file.write(json.dumps(parsed, indent=4, ensure_ascii=False))

    def saveSummary(self):
        jsonobj = { "TotalInvestmentAmount" : str(self.TotalInvestmentAmount), "Balance" : str(self.Balance), "Yield": str(self.Yield)}
        with open("result_summary.json", "w") as text_file:
            text_file.write(json.dumps(jsonobj, indent=4))

        

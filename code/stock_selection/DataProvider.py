from QuantDB import QuantDB
from typing import List

class DataProvider:
    DB = None

    def __init__(self):
        self.Name = "Default"
        self.DB = QuantDB()

    def __repr__(self):
        return self.Name
    
    def initialize(self):
        return self.DB.connect()
    
    def close(self):
        if( self.DB ):
            self.DB.close()
            self.DB = None

    def findFS(self, columns: List[str], year: int, quarter: int, div: str): # a: str, b: str, times: int
        if( self.DB ):
            querystring = 'SELECT '
            for target in columns: 
                querystring = querystring + '"' + target + '",'
            querystring = querystring[:-1]    
            querystring = querystring + 'from "FinancialStatements" ' + 'WHERE ' + '"Year"=' + str(year) + ' and "Quarter"=' + str(quarter) + ' and "Div"=' + "'" + div + "'"
            return self.DB.searchData(querystring, columns) 

    def findAllFS(self, columns: List[str], year: int, quarter: int, div: str):
        if( self.DB ):
            querystring = 'SELECT '
            for target in columns: 
                querystring = querystring + '"' + target + '",'
            querystring = querystring[:-1]
            querystring = querystring + 'from "FinancialStatements" ' + 'WHERE ' + '"Year"=' + str(year) + ' and "Quarter"=' + str(quarter) + ' and "Div"=' + "'" + div + "'"
            return self.DB.searchData(querystring, columns)

    def findOneFS(self, columns: List[str], stockcode: str, year: int, quarter: int, div: str):
        if( self.DB ):
            querystring = 'SELECT '
            for target in columns: 
                querystring = querystring + '"' + target + '",'
            querystring = querystring[:-1]
            querystring = querystring + 'from "FinancialStatements" ' + 'WHERE ' + '"id"=' + "'" + stockcode + str(year) + str(quarter) + div + "'"
            return self.DB.searchData(querystring, columns)            
            
    def findSPbyID(self, columns: List[str], stockcode: str, stockdate: str):
        if( self.DB ):
            querystring = 'SELECT '
            for target in columns: 
                querystring = querystring + '"' + target + '",'
            querystring = querystring[:-1]    
            querystring = querystring + 'from "StockPrice" ' + 'WHERE ' + '"id"=' + "'" + stockcode + stockdate + "'"
            return self.DB.searchData(querystring, columns)   

    def findSP(self, columns: List[str], stockcode: str, stock_startdate: str, stock_enddate: str):
        if( self.DB ):
            querystring = 'SELECT '
            for target in columns: 
                querystring = querystring + '"' + target + '",'
            querystring = querystring[:-1]    
            querystring = querystring + 'from "StockPrice" ' + 'WHERE ' + '"StockCode"=' + "'" + stockcode + "'"  ' and "StockDate" >= ' + "'" + stock_startdate + "'" + ' and "StockDate" <= ' + "'" + stock_enddate + "' order by id asc"
            return self.DB.searchData(querystring, columns)    

    def findCompany(self, columns: List[str], stockcode: str):
        if( self.DB ):
            querystring = 'SELECT '
            for target in columns: 
                querystring = querystring + '"' + target + '",'
            querystring = querystring[:-1]    
            querystring = querystring + 'from "Company" ' + 'WHERE ' + '"StockCode"=' + "'" + stockcode + "'"
            return self.DB.searchData(querystring, columns)    
    
    def findStockName(self, stockcode: str):
        if( self.DB ):
            df_comapanys = self.findCompany(["StockName"], stockcode)
            if df_comapanys is None :
                return ''
            else :
                return df_comapanys["StockName"][0]

    
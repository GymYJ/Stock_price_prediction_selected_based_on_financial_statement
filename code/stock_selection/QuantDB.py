import psycopg2
import pandas as pd
from typing import List

class QuantDB:
    Name = 'Base'   
    Conn = None
    ConnectionStr = 'host=aifactory-test.cp90w5j6b2ld.ap-northeast-2.rds.amazonaws.com dbname=QuantDB user=quantdb password=quantdb'

    def __init__(self):
        self.Name = "Default"

    def __repr__(self):
        return self.Name
    
    def connect(self):
        self.Conn = None
        try:
            self.Conn = psycopg2.connect(self.ConnectionStr)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return False
        return True
    def searchData(self, query: str, columns: List[str]):
        cursor = self.Conn.cursor()
        try:
            cursor.execute(query)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            cursor.close()
            return None
        tupples = cursor.fetchall()
        cursor.close()
        df = pd.DataFrame(tupples, columns=columns)
        return df

    def searchDataOneRow(self, query: str):
        cursor = self.Conn.cursor()
        try:
            cursor.execute(query)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            cursor.close()
            return None
        row = cursor.fetchone()
        cursor.close()
        return row[0]

    def close(self):
        self.Conn.close()
import Strategy
import Trading
import Verification
import sys
import DataProvider

st = Strategy.Strategy()
tr = Trading.Trading()
ve = Verification.Verification()
db = DataProvider.DataProvider()

if db.initialize():
    print('db connection')

    st.db = db
    st.setStrategy()
    if st.searchData() == False:
        print("st.searchData error")
        sys.exit(-1)
    if st.setAdditionalData() == False:
        print("st.setAdditionalData error")
        sys.exit(-1)

    tr.df_all = st.df_all
    tr.db = db
    tr.setTrading()
    if tr.doTrading() == False:
        print("tr.doTrading error")
        sys.exit(-1)

    ve.TotalInvestmentAmount = tr.TotalInvestmentAmount
    ve.df_all = tr.df_all
    ve.setVerification()
    ve.doVerification()
    ve.saveResult()
    # ve.saveResulToJSON()
    ve.saveSummary()
else:
    print("db error")
db.close()

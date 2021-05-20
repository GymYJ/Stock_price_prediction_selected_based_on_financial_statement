import datetime
import Strategy
import Trading
import Verification
import sys
import DataProvider


def single():
    record = [0]
    # record = [18.91309, 17.8967, 17.14154, 16.07653, 16.03074]
    strategy_record = [[3, 0.7000000000000001, 10, 18.91309], [3, 0.7000000000000001, 11, 17.8967],
                       [3, 0.8, 11, 17.14154], [4, 0.7000000000000001, 11, 16.07653],
                       [3, 0.7000000000000001, 5, 16.03074]]
    st = Strategy.Strategy()
    tr = Trading.Trading()
    ve = Verification.Verification()
    db = DataProvider.DataProvider()
    if db.initialize():
        print('db connection')
        # print(db.findSP(['StockDate','Open'], '004990', '2019-04-11', '2019-12-31'))
        st.db = db
        st.setStrategy(10, 0, 1.5, 0)
        if (st.searchData() == False):
            print("st.searchData error")
            sys.exit(-1)
        if (st.setAdditionalData() == False):
            print("st.setAdditionalData error")
            sys.exit(-1)

        tr.df_all = st.df_all
        tr.db = db
        tr.setTrading()
        if (tr.doTrading() == False):
            print("tr.doTrading error")
            sys.exit(-1)

        ve.TotalInvestmentAmount = tr.TotalInvestmentAmount
        ve.df_all = tr.df_all

        ve.setVerification()
        ve.doVerification()
        ve.saveResult()
        # ve.saveResulToJSON()
        r, Yield = ve.saveSummary(record, 0)
    else:
        print("db error")
    db.close()


def multi():
    start = datetime.datetime.now()
    record = [0]
    strategy_record = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    num = 0
    st = Strategy.Strategy()
    tr = Trading.Trading()
    ve = Verification.Verification()
    db = DataProvider.DataProvider()
    for per in range(8):
        pbr = 1
        while pbr > 0.3:
            for roe in range(10, 20):
                if db.initialize():
                    print('db connection')
                    # print(db.findSP(['StockDate','Open'], '004990', '2019-04-11', '2019-12-31'))
                    st.db = db
                else:
                    print("db error")
                st.setStrategy(per, pbr, 1.2, roe)
                if (st.searchData() == False):
                    print("st.searchData error")
                    sys.exit(-1)
                if (st.setAdditionalData() == False):
                    print("st.setAdditionalData error")
                    sys.exit(-1)

                tr.df_all = st.df_all
                tr.db = db
                tr.setTrading()
                if (tr.doTrading() == False):
                    print("tr.doTrading error")
                    sys.exit(-1)

                ve.TotalInvestmentAmount = tr.TotalInvestmentAmount
                ve.df_all = tr.df_all
                ve.setVerification()
                ve.doVerification()
                ve.saveResult()
                # ve.saveResulToJSON()
                r, Yield = ve.saveSummary(record, num)
                if r:
                    for i in range(5):
                        if strategy_record[i][3] < Yield:
                            strategy_record.insert(i, [per, pbr, roe, Yield])
                            break
                    strategy_record.pop()
                    print(record, strategy_record)
                num += 1
            pbr -= 0.1
    db.close()
    end = datetime.datetime.now()
    print('time: ', end - start)
    print(strategy_record)


if __name__ == '__main__':
    single()
    # multi()

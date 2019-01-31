import os;
from finviz.screener import Screener

def get_screener_name():
    return 'movingUpScreener'

def dump_to_csv(dirName):

    if not os.path.exists(dirName):
        os.makedirs(dirName)

    filters = ['geo_usa','ta_change_u','ta_highlow20d_nh','ta_highlow50d_nh','ta_highlow52w_nh','ta_perf_dup']  # Shows companies in NASDAQ which are in the S&P500
    stock_list = Screener(filters=filters, order='ticker') 


    print((stock_list))
    stock_list.to_csv(dirName,get_screener_name())

#dump_to_csv('screenerOutput')
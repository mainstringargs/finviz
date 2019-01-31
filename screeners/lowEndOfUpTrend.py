import os;
from finviz.screener import Screener

def get_screener_name():
    return 'lowEndOfUpTrend'

def dump_to_csv(dirName):

    if not os.path.exists(dirName):
        os.makedirs(dirName)

    filters = ['sh_avgvol_o1000','ta_pattern_channelup','ta_perf_1wdown']  # Shows companies in NASDAQ which are in the S&P500
    stock_list = Screener(filters=filters, order='ticker') 

    print((stock_list))
    stock_list.to_csv(dirName,get_screener_name())

#dump_to_csv('screenerOutput')
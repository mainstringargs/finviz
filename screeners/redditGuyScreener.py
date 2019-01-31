import os;
from finviz.screener import Screener

def get_screener_name():
    return 'redditGuyScreener'

def dump_to_csv(dirName):

    if not os.path.exists(dirName):
        os.makedirs(dirName)

    filters = ['fa_eps5years_pos','fa_epsqoq_o20','fa_epsyoy_o25','fa_epsyoy1_o15','fa_estltgrowth_pos','fa_roe_o10','sh_instown_o10','ta_highlow52w_a50h','ta_rsi_nos50']  # Shows companies in NASDAQ which are in the S&P500
    stock_list = Screener(filters=filters, order='ticker') 

    print((stock_list))
    stock_list.to_csv(dirName,get_screener_name())

#dump_to_csv('screenerOutput')
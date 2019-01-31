import os;
from finviz.screener import Screener

def get_screener_name():
    return 'redditCANSLIM'

def dump_to_csv(dirName):

    if not os.path.exists(dirName):
        os.makedirs(dirName)


#https://www.reddit.com/r/CANSLIM/comments/6rfupr/finviz_screeners_settings/

#https://finviz.com/screener.ashx?v=111&f=cap_small,fa_eps5years_o20,fa_epsqoq_o20,fa_epsyoy_o20,fa_sales5years_o20,fa_salesqoq_o20,sh_curvol_o200&ft=4

    filters = ['cap_small','fa_eps5years_o20','fa_epsqoq_o20','fa_epsyoy_o20','fa_sales5years_o20','fa_salesqoq_o20','sh_curvol_o200']  # Shows companies in NASDAQ which are in the S&P500
    stock_list = Screener(filters=filters, order='ticker') 

    print((stock_list))
    stock_list.to_csv(dirName,get_screener_name())

#dump_to_csv('screenerOutput')
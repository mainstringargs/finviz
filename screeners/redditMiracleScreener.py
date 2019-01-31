from finviz.screener import Screener




import os;
from finviz.screener import Screener

def get_screener_name():
    return 'redditMiracleScreener'

def dump_to_csv(dirName):

    if not os.path.exists(dirName):
        os.makedirs(dirName)

#https://www.reddit.com/r/stocks/comments/79e9zm/finviz_screener_criteria/

#https://www.finviz.com/screener.ashx?v=111&f=fa_eps5years_pos,fa_epsqoq_o20,fa_epsyoy_o25,fa_epsyoy1_o15,fa_estltgrowth_pos,fa_roe_o15,sh_instown_o10,sh_price_o15,ta_highlow52w_a90h,ta_rsi_nos50&ft=4
#https://www.finviz.com/screener.ashx?v=111&f=fa_eps5years_pos,fa_epsqoq_o20,fa_epsyoy_o25,fa_epsyoy1_o15,fa_estltgrowth_pos,fa_roe_o15,sh_instown_o10,ta_highlow52w_a90h,ta_rsi_nos50&ft=4

	
    filters = ['fa_eps5years_pos','fa_epsqoq_o20','fa_epsyoy_o25','fa_epsyoy1_o15','fa_estltgrowth_pos','fa_roe_o15','sh_instown_o10','ta_highlow52w_a90h','ta_rsi_nos50']  # Shows companies in NASDAQ which are in the S&P500
    stock_list = Screener(filters=filters, order='ticker') 

    print((stock_list))
    stock_list.to_csv(dirName,get_screener_name())

#dump_to_csv('screenerOutput')
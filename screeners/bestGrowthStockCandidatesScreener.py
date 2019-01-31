import os;
from finviz.screener import Screener

def get_screener_name():
    return 'bestGrowthStockCandidates'

def dump_to_csv(dirName):

    if not os.path.exists(dirName):
        os.makedirs(dirName)

#http://www.winninginvesting.com/small_cap_screen.htm
#https://finviz.com/screener.ashx?v=111&f=cap_small,fa_epsyoy_o15,fa_epsyoy1_o15,fa_estltgrowth_o15,fa_peg_u1,fa_roe_pos,geo_usa,sh_avgvol_o500,sh_instown_o40&ft=4

    filters = ['cap_small','fa_epsyoy_o15','fa_epsyoy1_o15','fa_estltgrowth_o15','fa_peg_u1','fa_roe_pos','geo_usa','sh_avgvol_o500','sh_instown_o40']  # Shows companies in NASDAQ which are in the S&P500
    stock_list = Screener(filters=filters, order='ticker') 


    print((stock_list))
    stock_list.to_csv(dirName,get_screener_name())

#dump_to_csv('screenerOutput')
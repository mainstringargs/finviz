import os;
from finviz.screener import Screener

def get_screener_name():
    return 'growthAcceleratedEarnings'

def dump_to_csv(dirName):

    if not os.path.exists(dirName):
        os.makedirs(dirName)

    filters = ['fa_debteq_u0.5','fa_epsqoq_o25','fa_roe_o15','fa_salesqoq_o20','sh_avgvol_o200','sh_instown_o60','sh_price_o5','sh_short_u5']  # Shows companies in NASDAQ which are in the S&P500
    stock_list = Screener(filters=filters, order='ticker') 

    print((stock_list))
    stock_list.to_csv(dirName,get_screener_name())
	
def get_current_dataframe():
    filters = ['fa_debteq_u0.5','fa_epsqoq_o25','fa_roe_o15','fa_salesqoq_o20','sh_avgvol_o200','sh_instown_o60','sh_price_o5','sh_short_u5']  # Shows companies in NASDAQ which are in the S&P500
    stock_list = Screener(filters=filters, order='ticker') 
    print(type(stock_list));


#dump_to_csv('screenerOutput')
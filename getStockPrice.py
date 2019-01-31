# load the stock_info module from yahoo_fin
from yahoo_fin import stock_info as si

# get Apple's live quote price
print(si.get_live_price("AAPL"))

# or Amazon's
print(si.get_live_price("QQQ"))
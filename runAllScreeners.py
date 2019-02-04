import screeners.movingUpScreener as movingUpScreener
import screeners.lowEndOfUpTrend as lowEndOfUpTrend
import screeners.redditGuyScreener as redditGuyScreener
import screeners.preMovingUp as preMovingUp
import screeners.growthAcceleratedEarnings as growthAcceleratedEarnings
import screeners.looseCANSLIM as looseCANSLIM
import screeners.redditCANSLIM as redditCANSLIM
import screeners.redditMiracleScreener as redditMiracleScreener
import screeners.bestGrowthStockCandidatesScreener as bestGrowthStockCandidatesScreener
import screeners.stocksTrendingUpInAStrongChannel as stocksTrendingUpInAStrongChannel
import screeners.oversoldStocksBouncingAtTechnicalSupport as oversoldStocksBouncingAtTechnicalSupport
import screeners.greenPlus15 as greenPlus15
import screeners.fullCanSlim as fullCanSlim
import screeners.red as red
from datetime import datetime
import time;


def dumpAllScreeners(dirName):

    try:
        print("Getting CSV for "+red.get_screener_name());
        red.dump_to_csv(dirName);
    except:
	    print("Exception getting "+red.get_screener_name());
		
    try:
        print("Getting CSV for "+fullCanSlim.get_screener_name());
        fullCanSlim.dump_to_csv(dirName);
    except:
	    print("Exception getting "+fullCanSlim.get_screener_name());

    try:
        print("Getting CSV for "+greenPlus15.get_screener_name());
        greenPlus15.dump_to_csv(dirName);
    except:
	    print("Exception getting "+greenPlus15.get_screener_name());
		
    try:
        print("Getting CSV for "+oversoldStocksBouncingAtTechnicalSupport.get_screener_name());
        oversoldStocksBouncingAtTechnicalSupport.dump_to_csv(dirName);
    except:
	    print("Exception getting "+oversoldStocksBouncingAtTechnicalSupport.get_screener_name());
		
    try:
        print("Getting CSV for "+stocksTrendingUpInAStrongChannel.get_screener_name());
        stocksTrendingUpInAStrongChannel.dump_to_csv(dirName);
    except:
	    print("Exception getting "+stocksTrendingUpInAStrongChannel.get_screener_name());
		
    try:
        print("Getting CSV for "+bestGrowthStockCandidatesScreener.get_screener_name());
        bestGrowthStockCandidatesScreener.dump_to_csv(dirName);
    except:
	    print("Exception getting "+bestGrowthStockCandidatesScreener.get_screener_name());
		
  #  try:
   #     print("Getting CSV for "+movingUpScreener.get_screener_name());
   #     movingUpScreener.dump_to_csv(dirName);
   # except:
	#    print("Exception getting "+movingUpScreener.get_screener_name());

    try:
        print("Getting CSV for "+lowEndOfUpTrend.get_screener_name());
        lowEndOfUpTrend.dump_to_csv(dirName);
    except:
        print("Exception getting "+lowEndOfUpTrend.get_screener_name());	

    try:
        print("Getting CSV for "+redditGuyScreener.get_screener_name());
        redditGuyScreener.dump_to_csv(dirName);
    except:
	    print("Exception getting "+redditGuyScreener.get_screener_name());	

    try:
        print("Getting CSV for "+preMovingUp.get_screener_name());
        preMovingUp.dump_to_csv(dirName);
    except:
	    print("Exception getting "+preMovingUp.get_screener_name());	

    try:
        print("Getting CSV for "+growthAcceleratedEarnings.get_screener_name());
        growthAcceleratedEarnings.dump_to_csv(dirName);
    except:
	    print("Exception getting "+growthAcceleratedEarnings.get_screener_name());	

    try:
        print("Getting CSV for "+looseCANSLIM.get_screener_name());
        looseCANSLIM.dump_to_csv(dirName);
    except:
	    print("Exception getting "+looseCANSLIM.get_screener_name());	

    try:
        print("Getting CSV for "+redditCANSLIM.get_screener_name());
        redditCANSLIM.dump_to_csv(dirName);
    except:
	    print("Exception getting "+redditCANSLIM.get_screener_name());	

    try:
        print("Getting CSV for "+redditMiracleScreener.get_screener_name());
        redditMiracleScreener.dump_to_csv(dirName);
    except:
	    print("Exception getting "+redditMiracleScreener.get_screener_name());	
	


dirName = "screenerOutput";

dumpedDataAfternoon = False
dumpedDataMorning = False

while True:
    now = datetime.now().strftime('%H%M')
    weekday = datetime.now().isoweekday()

    if (weekday <= 5 and now < '0800' and dumpedDataAfternoon):	
        print("Flipping Afternoon boolean");
        dumpedDataAfternoon = False
	
    if (not dumpedDataAfternoon and weekday <= 5 and now >= '1505' and now <= '1515'):
        dumpAllScreeners(dirName);
        dumpedDataAfternoon=True
		
    if (weekday <= 5 and now > '0820' and now < '0830' and not dumpedDataMorning):
        dumpAllScreeners(dirName);
        dumpedDataMorning=True	
	
    if (dumpedDataMorning and weekday <= 5 and now >= '1505'):
        print("Flipping Morning boolean");
        dumpedDataMorning = False		
	
    print("Sleeping at "+str(now) + " "+str(weekday));	
    time.sleep(60 * 5)
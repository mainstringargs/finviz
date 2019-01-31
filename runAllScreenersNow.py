import screeners.movingUpScreener as movingUpScreener
import screeners.lowEndOfUpTrend as lowEndOfUpTrend
import screeners.redditGuyScreener as redditGuyScreener
import screeners.preMovingUp as preMovingUp
import screeners.growthAcceleratedEarnings as growthAcceleratedEarnings
import screeners.looseCANSLIM as looseCANSLIM
import screeners.redditCANSLIM as redditCANSLIM
import screeners.redditMiracleScreener as redditMiracleScreener
from datetime import datetime
import time;

def dumpAllScreeners(dirName):

    try:
        print("Getting CSV for "+movingUpScreener.get_screener_name());
        movingUpScreener.dump_to_csv(dirName);
    except:
	    print("Exception getting "+movingUpScreener.get_screener_name());

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

dumpAllScreeners(dirName);

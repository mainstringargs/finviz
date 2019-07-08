import screeners.looseCANSLIMFullUSA as looseCANSLIMFullUSA

from datetime import datetime
import time;


def dumpAllScreeners(dirName):

    try:
        print("Getting CSV for "+looseCANSLIMFullUSA.get_screener_name());
        looseCANSLIMFullUSA.dump_to_csv(dirName);
    except:
	    print("Exception getting "+looseCANSLIMFullUSA.get_screener_name());



dirName = "looseCANSLIMFullUSA";

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
import screeners.looseCANSLIMFullUSA as looseCANSLIMFullUSA

from datetime import datetime
import time;


def dumpAllScreeners(dirName):

    print("Getting CSV for "+looseCANSLIMFullUSA.get_screener_name());
    looseCANSLIMFullUSA.dump_to_csv(dirName);



dirName = "looseCANSLIMFullUSA";


dumpAllScreeners(dirName);

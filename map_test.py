from MoonMap_memory import MoonMap
from datetime import datetime
from collections import OrderedDict
import matplotlib.pyplot as plt


def test(size, fill):
    """using for loops this method sets, loads, gets and deletes data"""
    map = MoonMap(size)
    __test_set(fill, map)
    __test_load(map)
    __test_get(fill, map)
    __test_delete(fill, map)
    __test_load(map)

def __test_set(fill, memap):
    """sets Map with values from 0 to the fill value"""
    x = datetime.now()
    for i in range(fill):
        memap.boolean_set(("yumm" + str(i)), i)
    y = datetime.now()
    sec = (y - x).total_seconds()
    sec_per_set = sec / fill
    micsec = sec_per_set * 1000000
    print("It took {} microseconds to set values set in {} seconds".format(fill, micsec))
    return micsec

def __test_delete(fill, memap):
    """Enter the number of values to delete from MoonMap, values are deleted in a loop starting from zero
     to the fill value"""
    x = datetime.now()
    for i in range(fill):
        memap.delete(("yumm" + str(i)))
    y = datetime.now()
    sec = (y - x).total_seconds()
    sec_per_delete = sec/fill
    micsec = sec_per_delete * 1000000
    print("It took an average time of {} to delete each item from the map".format(micsec))
    return micsec

def __test_get(fill, memap):
    """Retrieves values from 0 to the fill value"""
    x = datetime.now()
    for i in range(fill):
        memap.delete(("yumm" + str(i)))
    y = datetime.now()
    sec =  ( (y - x).total_seconds() )
    sec = (y - x).total_seconds()
    sec_per_get = sec / fill
    micsec = sec_per_get * 1000000
    print("Toook an average of {} microseconds to get each item".format(micsec))
    return micsec

def __test_load(memap):
    """Finds the the time it took to calculate load in microseconds (usually ZERO)"""
    x = datetime.now()
    for i in range(1000):
        memap.load()
    y = datetime.now()
    sec = (y - x).total_seconds()
    sec_per_load = sec / 1000
    micsec = sec_per_delete * 1000000
    print("Load is {}, it took {} microseconds to load".format(memap.load(), micsec))
    return micsec


###EXTRA METHODS TO VISUALIZE efficency, NOT NEEDED FOR TESTING
def run_time_graph(size):
    """NOT NEEDED FOR TESTING
    This Method was used to generate scatter plots that showed algorythm efficency for setting,
    retrieving and deleting values from a MoonMap with size 1000"""
    map = MoonMap(size)
    set = OrderedDict()
    get = OrderedDict()
    delete = OrderedDict()
    for i in range(200, size):
        set[i] = ( __test_set(i, map)/float(i) ) * 1000000
        get[i] = (__test_get(i, map)/float(i) ) * 1000000
        delete[i] = (__test_delete(i, map)/float(i) ) * 1000000

        print(i)

    __plot(set, "Set Speed (Map Size {})".format(size))
    __plot(get, "Get Speed (Map Size {})".format(size) )
    __plot(delete, "Delete Speed (Map Size {})".format(size))

def __plot( dict1, title):
    """Used to plot and format graphs"""
    plt.title(title)
    plt.xlabel("Run Time (microsecondsS)")
    plt.ylabel("Number of Items Retreived")
    plt.ylim(0, max(dict1.values()))
    plt.xlim(min(dict1.keys()), max(dict1.keys()) )
    x1, y1 = zip(*dict1.items())

    plt.scatter(x1, y1)
    plt.show()


#run_time_graph(1000)
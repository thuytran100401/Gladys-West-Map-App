import io
import json

"""
    Student: Mercedez Tran
    Module: gladysSatellite
    Description: This module opens and reads the altitude data file from disk using the readSat function. 
"""

# start code by Mercedez Tran
def readSat(sat, pathToJSONDataFiles):
    """
        reads satellite data from a json file
        Students do NOT need to change the readSat function.
    """
    # data file path
    fileName = sat + "-satellite.json"
    filePath = pathToJSONDataFiles + "/" + fileName
    
    # open the file
    try: 
        fileHandle = open(filePath)
    except IOError:
        print("Error: Unable to open the file " + filePath)
        raise IOError
    
    # read the file
    data = json.load(fileHandle)

    return data


def gpsValue(x, y, sat):
    value = 0
    """
       It uses the satellite to pinpoint user's location and desired location to find best possible route
    """
    pathToJSONDataFiles = './data'

    # read the satellite data
    data = readSat(sat, pathToJSONDataFiles)

    # get gps value from the file
   
    for i in data:
        if i["x"]== x and i["y"] == y:
            value = i["value"]
    return value 

#end code by Mercedez Tran

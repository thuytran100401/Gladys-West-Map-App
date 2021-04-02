import io
import json

"""
    Student: Nhi Pham
    Module: gladysSatellite
    Description: This module reads satellite data from a json file and find a matching x, y to return the value. 
"""

def readSat(sat, pathToJSONDataFiles):
    """
        reads satellite data from a json file
        Students do NOT need to change the readSat function.
    """
    # data file path
    fileName = sat + "-satellite.jon"
    filePath = pathToJSONDateFiles + "/" + fileName
    
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
    """
        read the files
        find matching x and y
        return value for each sat
    """
    pathToJSONDataFiles = "C:/Users/thuy/Downloads/Gladys-West-Map-App/data"

    # read the satellite data
    data = readSat(sat, pathToJSONDataFiles)

    # get gps value from the file
    for i in data:
        if x == i['x'] and y == i['y']:
            value == i['value']
        return value 



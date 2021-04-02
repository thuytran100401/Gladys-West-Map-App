import io
import math
import gladysSatellite as satellite

"""
     Student: Truc Nguyen
     Module: gladysCompute
     Description: This module preforms the underlying calculations to figure out the distance between the current position (x,y) and destination position (x,y)
"""
# start of code by Lo Tuan
def gpsAverage(x, y):
    
     value = satellite.gpsValue(x, y, "altitude") + satellite.gpsValue(x, y, 
     "longitude") + satellite.gpsValue(x, y, "latitude") + satellite.gpsValue(x, y, "time")
     average = value / 4
     return average
 
def distance(current, destination):

     currentAverage = gpsAverage(current[0], current[1])
     destinationAverage = gpsAverage(destination[0], destination[1])
     distance = math.sqrt((currentAverage**2) + (destinationAverage**2))

     return distance
# end of code by Lo Tuan

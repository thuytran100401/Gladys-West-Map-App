import io
import math
import gladysSatellite as satellite

"""
     Student: Truc Nguyen
     Module: gladysCompute
     Description: This module preforms the underlying calculations to figure out the distance between the current position (x,y) and destination position (x,y)
"""
#start code by Truc Nguyen
def gpsAverage(x, y):
     """
          value = 𝑔𝑝𝑠𝑉𝑎𝑙𝑢𝑒(𝑥,𝑦,"𝑙𝑎𝑡𝑖𝑡𝑢𝑑𝑒")+𝑔𝑝𝑠𝑉𝑎𝑙𝑢𝑒(𝑥,𝑦,"𝑙𝑜𝑛𝑔𝑖𝑡𝑢𝑑𝑒")+𝑔𝑝𝑠𝑉𝑎𝑙𝑢𝑒(𝑥,𝑦,"𝑎𝑙𝑡𝑖𝑡𝑢𝑑𝑒")+𝑔𝑝𝑠𝑉𝑎𝑙𝑢𝑒(𝑥,𝑦,"𝑡𝑖𝑚𝑒")
     """
     value = satellite.gpsValue(x, y, "altitude") + satellite.gpsValue(x, y, 
     "longitude") + satellite.gpsValue(x, y, "latitude") + satellite.gpsValue(x, y, "time")
     average = value / 4
     return average
 
def distance(current, destination):
     """
          Computes the distance between the current position and the destination position using the following formulas.
          Distance = square root(gpsAverage(x current, y current) square + gpsAverage(x destination, ydestination) square)
     """
     currentAverage = gpsAverage(current[0], current[1])
     destinationAverage = gpsAverage(destination[0], destination[1])
     distance = math.sqrt((currentAverage**2) + (destinationAverage**2))

     return distance
# end of code by Truc Nguyen

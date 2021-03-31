import io
import gladysSatellite as satellite

"""
     Student: Lo Tuan
     Module: gladysCompute
     Description: This module computes the distance between the current position and the destination position.
"""
# start of code by Lo Tuan
def gpsAverage(x,y):
"""
Calculate average gps value of latitude, longitude, altitude, and time
"""
value = satellite.gpsValue(x,y,"altitude")+satellite.gpsValue(x,y,"longitude")+satellite.gpsValue(x,y,"latitude")+satellite.gpsValue(x,y,"time")
average = value/4
return average
 
def distance(current,destination):
"""
Calculate difference of average gps values of current position and destination position
"""
 
distance = gpsAverage(xdestination,ydestination)-gpsAverage(xcurrent,ycurrent)
return distance
# end of code by Lo Tuan

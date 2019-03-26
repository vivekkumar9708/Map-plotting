# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

m = Basemap(projection='mill',llcrnrlat=-90,urcrnrlat=90,\
            llcrnrlon=-180,urcrnrlon=180,resolution='h')
m.drawcoastlines()
m.drawcountries()
m.drawstates()
m.drawrivers()

m.fillcontinents(color = 'r', lake_color = 'b')
m.drawmapboundary(fill_color = 'b')
m.bluemarble()
lat = 30,31,34,33,32
lon = -103,-110,-107,-111,-115


lat2 = 40,33,44,31,30
lon2 = -113,-100,-102,-111,-112

x,y = m(lon,lat)
m.plot(x,y,'ro',markersize=20,alpha=.5)

x,y = m(lon2,lat2)
m.plot(x,y,'go',markersize=20,alpha=.5)

plt.title("GEO PLOTTING!")
plt.show()
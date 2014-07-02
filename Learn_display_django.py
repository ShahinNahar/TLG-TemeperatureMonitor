# import datetime
# import regular expression for reading the file name without the escape
# character "\"
import re
# import num py
import numpy as np
from matplotlib.dates import date2num, DateFormatter
from pylab import *

import matplotlib.pyplot as plt

from scipy.interpolate import spline

#with open (r"S:\Customers\TLG\IR&D\004 - 2014 Summer Internship\02 - Data Transfer\From Mike Dinh\TempHIDData_TLG24_2014_06.txt", 'r') as temperature_file:

filename =  r"S:\Customers\TLG\IR&D\004 - 2014 Summer Internship\02 - Data Transfer\From Mike Dinh\TempHIDData_TLG24_2014_06.txt"
with open (filename, 'r') as temperature_file:

    data = {'datetime': [],
            'temperature': [],
            }

    for line in temperature_file:


        if '#' not in line:
            split_string = re.split('\t', line)
            data['datetime'].append(split_string[0])
            data['temperature'].append(float(split_string[1]))


    print data['datetime'][0]
    print len(data['temperature'])


#x = np.array(range(0,len(data['temperature'])))
x = range(0,len(data['temperature']))

y = np.array(data['temperature'])

#x_smooth = np.linspace(x.min(), x.max(),300)
#y_smooth = spline(x,y,x_smooth)

plt.plot(x, y, linewidth = 2)
xlabel ("date and time (t)")
ylabel ("temperatute (c)")
title("Server room temperate: time vs temperature")
grid (True)
plt.show()


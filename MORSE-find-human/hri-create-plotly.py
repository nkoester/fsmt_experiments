## EXPERIMENTAL PLOTLY FEATURE ##

import csv
import sys
sys.path.append("/media/FSM-Lab/releases/precise/x64/lib/python2.7/site-packages")
import plotly

py = plotly.plotly(username='flier', key='pwp34m9niq')
colors = ['rgb(0,0,238)','rgb(67,67,67)','rgb(111,168,220)']

if not len(sys.argv) > 1:
    print "No CSV file given"
    sys.exit(1)

x = []
y = []

with open(sys.argv[1], 'rb') as csvfile:
     reader = csv.reader(csvfile, delimiter=',')
     for row in reader:
         x.append(row[3])
         y.append(row[2])

data = []
data.append({'x':x,'y':y,'type':'bar','marker':{'color':colors[0]}})

l={'xaxis':{"zeroline":False},'yaxis':{"zeroline":False},'showlegend':False}

py.plot(data,layout=l)

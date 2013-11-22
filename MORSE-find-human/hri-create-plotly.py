## EXPERIMENTAL PLOTLY FEATURE ##

import csv
import sys
# If you installed plotly in your std prefix you may comment this line. 
# To get plotly just execute: pip install plotly
sys.path.append("/media/FSM-Lab/releases/precise/x64/lib/python2.7/site-packages")
import plotly

if not len(sys.argv) > 2:
    print "No CSV file, or API Key given"
    sys.exit(1)

py = plotly.plotly(username='flier', key=sys.argv[2])
colors = ['rgb(0,0,238)','rgb(67,67,67)','rgb(111,168,220)']

x = []
y = []

with open(sys.argv[1], 'rb') as csvfile:
     reader = csv.reader(csvfile, delimiter=',')
     for row in reader:
         x.append(row[3])
         y.append(row[2])
	
data = []
data.append({'x':x,'y':y})

# l={'xaxis':{"zeroline":False},'yaxis':{"zeroline":False},'showlegend':False}

l = {'width':500,'height':500,'showlegend':False,'autosize':False}

py.plot(data,layout=l)

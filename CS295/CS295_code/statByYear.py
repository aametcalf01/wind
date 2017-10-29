import os
import sys
import pandas as pd
import numpy as numpy

stat = sys.argv[1]
dest = sys.argv[2]
y1 = 1902
y2 = 2015
ys = range(y1,y2+1)

cols = ['YR--MODAHRMN','DIR','SPD','GUS','TEMP','SLP']
data = pd.DataFrame(columns=['Lat','Lon','Ele']+cols)

for y in ys :
    dat = pd.read_csv('/users/a/a/aametcal/CS295/rawData/'+str(y)+'/'+stat+'-'+str(y)+'.txt',delim_whitespace=True)
    nDat = dat[cols]
    nDat.insert(loc=0,column='Lat', value=float(temp[0]))
    nDat.insert(loc=1,column='Lon', value=float(temp[1]))
    nDat.insert(loc=2,column='Ele', value=float(temp[2]))
    data = pd.concat([data,nDat])

data.to_csv(dest)

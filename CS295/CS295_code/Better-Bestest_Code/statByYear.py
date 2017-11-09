import os
import sys
import pandas as pd
import numpy as numpy

def getLatLonElev():
        dic ={}
        f = open("/users/a/a/aametcal/wind/readmeDocs/isd-history.csv")
        counter = 0;
        for line in f:
                lst = line.split(',')
                for i in range(len(lst)):
                        lst[i] = lst[i].strip().strip('"')
                code = lst[0]+"-"+lst[1] #create the USAF#-WBAN# code
                if counter !=0:
                        dic[code] =(lst[6],lst[7],lst[8],lst[9],lst[10])	
                counter+=1
        f.close()
        flag = 0
        exs = []
        for station in dic.keys():
                for i in dic[station]:
                        if i == '':
                                flag+=1
                if flag !=0:
                        exs.append(station)
                flag = 0
        for ex in exs :
                dic.pop(ex)
        return dic

dic = getLatLonElev()

stat = sys.argv[1]
dest = sys.argv[2]
y1 = 1902
y2 = 2015
ys = range(y1,y2+1)

if stat in dic.keys() :
    cols = ['YR--MODAHRMN','DIR','SPD','GUS','TEMP','SLP']
    data = pd.DataFrame(columns=['Lat','Lon','Ele']+cols)

    for y in ys :
        if os.path.exists('/users/a/a/aametcal/wind/rawData/'+str(y)) :
            if os.path.exists('/users/a/a/aametcal/wind/rawData/'+str(y)+'/'+stat+'-'+str(y)+'.txt') :
                    dat = pd.read_csv('/users/a/a/aametcal/wind/rawData/'+str(y)+'/'+stat+'-'+str(y)+'.txt',delim_whitespace=True)
                    print(str(y))
                    nDat = dat[cols]
                    temp = dic[stat]
                    nDat.insert(loc=0,column='Lat', value=float(temp[0]))
                    nDat.insert(loc=1,column='Lon', value=float(temp[1]))
                    nDat.insert(loc=2,column='Ele', value=float(temp[2]))
                    data = pd.concat([data,nDat])

    data.to_csv(dest)
else :
    print('Missing Station Info')

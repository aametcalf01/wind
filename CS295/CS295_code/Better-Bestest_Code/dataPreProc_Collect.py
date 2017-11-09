import os
import sys
import pandas as pd
import numpy as numpy

def getLatLonElev():
        dic ={}
        f = open("/users/a/a/aametcal/wind/CS295/readmeDocs/isd-history.csv")
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

y1 = 1902
y2 = 2015
ys = range(y1,y2+1)

src = '/users/a/a/aametcal/wind/rawData/'+year
dest = sys.argv[1]
lats = (float(sys.argv[2]),float(sys.argv[3]))
lons = (float(sys.argv[4]),float(sys.argv[5]))
cols = ['YR--MODAHRMN','DIR','SPD','GUS','TEMP','ALT'] # write in list of column strings

if not os.path.exists(dest):
        os.makedirs(dest)

for y in ys :
        src = '/users/a/a/aametcal/wind/rawData/'+str(y)
        data = pd.DataFrame(columns=['Lat','Lon','Ele']+cols)
        for root, dirs, files in os.walk(src,topdown=True):
                for file in files:
                        test = os.path.join(file)
        ##                print(test)
                        ref = test[0:12]
        ##                print(ref)
                        if ref in dic.keys() :
                                temp = dic[ref]
                                if (lats[0] < float(temp[0]) < lats[1]) and (lons[0] < float(temp[1]) < lons[1]) and not (temp[3][:4] == year or temp[4][:4] == year) :
                                        print(test)
                                        dat = pd.read_csv('/users/a/a/aametcal/wind/rawData/'+year+'/'+test,delim_whitespace=True)
                                        nDat = dat[cols]
                                        nDat.insert(loc=0,column='Lat', value=float(temp[0]))
                                        nDat.insert(loc=1,column='Lon', value=float(temp[1]))
                                        nDat.insert(loc=2,column='Ele', value=float(temp[2]))
                                        data = pd.concat([data,nDat])
        data.to_csv(dest+'/'+str(y)+'.txt')                        





                        

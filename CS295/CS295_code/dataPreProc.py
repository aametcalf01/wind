import os
import sys
import fnmatch
import pandas as pd
import numpy as numpy

#This code takes as system arguments: year, file destination and file name, lower lattitude, upper lattitude, western longitude, easter longitude

#Returns a .csv file with all of the specified columns for the specified region for one year

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

#System argument number 1 
year = sys.argv[1]

src = '/users/a/a/aametcal/wind/rawData/'+year

#System argument number 2 file destination
dest = sys.argv[2]

#system arguments 3-6 are the lat/lon coords
lats = (float(sys.argv[3]),float(sys.argv[4]))
lons = (float(sys.argv[5]),float(sys.argv[6]))
cols = ['YR--MODAHRMN','DIR','SPD','GUS','TEMP','SLP'] # write in list of column strings

data = pd.DataFrame(columns=['Lat','Lon','Ele']+cols)
for root, dirs, files in os.walk(src,topdown=True):
        for file in files:
##                path = os.path.join(root+file)
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
data.to_csv(dest)

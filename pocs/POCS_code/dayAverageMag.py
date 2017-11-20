import numpy as np
import pandas as pd
import datetime
import pytz

def year(x):
    stringDate = str(x).strip()
    yr = stringDate[0:4]
    return yr

def month(x):
    stringDate = str(x).strip()
    mo = stringDate[4:6]
    return mo

def day(x):
    stringDate = str(x).strip()
    da = stringDate[6:8]
    return da

def hour(x):
    stringDate = str(x).strip()
    hr = stringDate[8:10]
    return hr

def min(x): 
    stringDate = str(x).strip()
    mn = stringDate[10:12]
    return mn



path ="/users/a/a/aametcal/wind/pocs/data/"
data = pd.read_csv(path+"mountWashington.txt")    
print(data.sample(8))

date = data['YR--MODAHRMN'][0]

print("date: ",date)
print(year(date))
print(month(date))

print(day(date))

print (hour(date))


print(min(date))

dateobj = datetime.datetime.strptime(str(date),'%Y%m%d%H%M')
print(dateobj)

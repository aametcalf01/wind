import numpy as np
import pandas as pd
import datetime
import os


file = os.getcwd()+"/totalDataUpperMidwest.txt"
dat = pd.read_csv(file,header =None)
dat.columns = ['First','Lat','Lon','Elevation','Date','Dir','Spd','Gus','Temp','Slp']
dat = dat.drop(['First','Elevation','Dir','Gus','Temp','Slp'],axis = 1)
dat = dat.sample(1000000)
print(dat.head())

dat.to_csv("FinalUpperMidwest.txt")

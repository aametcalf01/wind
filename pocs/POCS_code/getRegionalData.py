import glob
import numpy as np
import pandas as pd
import datetime

file_=open("totalDataUpperMidwest.txt","w")
for filename in glob.iglob('/users/a/a/aametcal/wind/pocs/data/upperMidwest/**/*.txt',recursive = True):
    f = open(filename,"r")
    next(f)
    file_.writelines(f.readlines())
    f.close()
file_.close()

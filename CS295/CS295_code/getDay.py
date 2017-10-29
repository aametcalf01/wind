import numpy as np
import pandas as pd


path = '/users/a/a/aametcal/CS295/procData/'
f = path+ '2015FinYo.txt'

data = pd.read_csv(f)    
print(data.sample(8))
print (data.shape)
print(data[:][0])


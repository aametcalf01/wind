import os
import sys
import numpy as numpy

def timeAvg(ls) :
    


src = sys.argv[1]
dest = sys.argv[2]

#cols = ['Lat','Lon','Ele']+['YR--MODAHRMN','DIR','SPD','GUS','TEMP','ALT']

with open(src) as f:
    contentI = f.readlines()

data = []

content = [contentI[x].split(',') for x in range(len(contentI))]

loc = content[1][1:3]
d = content[1][4]
temp = []
temp.append(content[1][4:9])
i=2
while (i < len(content)) :
    if content[i][1:3]==loc and content[i][4][0:8]==d[0:8]:
        temp.append(content[i][4:9])
    elif len(temp)>0 :
        eph = loc+[d[0:8]]
        for j in range(len(temp)) :
            temp[j][0] = float(temp[j][0][8:10])*60+float(temp[j][0][10:])
        evan = [[temp[x][0],temp[x][1],temp[x][2]] for x in range(len(temp))]
        dels = []
        for j in range(len(evan)) :
            if 'x' in evan[j][1] or 'x' in evan[j][2] :
                dels.append(j)
        dels.reverse()
        for j in dels :
            del evan[j]
        angs = np.pi/180*np.array([float(evan[x][1]) for x in range(len(evan))])
        vecs = []
        for j in range(len(evan)) :
            vecs.append(float(evan[j][2])*np.array([np.sin(angs[j]),np.cos(angs[j])]))
        avgWD = timeAvg([[evan[x][0],vecs[x]] for x in range(len(evan))])
        eph.append(avgWD)

        for j in range(3,6) :
            evan = [[temp[x][0],temp[x][j]] for x in range(len(temp))]
            dels = []
            for k in range(len(evan)) :
                if 'x' in evan[k][j]:
                    dels.append(k)
            dels.reverse()
            for k in dels :
                del evan[k]
            evan2 = [[evan[x][0],float(evan[x][1])] for x in range(len(evan))]
            eph.append(timeAvg(evan2))

        data.append(eph)
        
        
        loc = content[i][1:3]
        d = content[i][4]
        temp = []
        temp.append(content[i][5:9])
        i+=1
    else :
        print('DaFuq?')
        i+=1

# WRITE DATA
    

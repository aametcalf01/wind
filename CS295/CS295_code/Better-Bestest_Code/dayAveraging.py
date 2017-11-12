import os
import sys
import numpy as np
##import pandas as pd

def timeAvg(ls) :
##    lsArr = np.array(ls)
##    ws = []
##    ws.append((lsArr[0,0]+lsArr[1,0])/2 - lsArr[0,0]+30)
##    for i in range(1,len(ls)-1) :
##        ws.append(((lsArr[i,0]+lsArr[i+1,0]) - (lsArr[i,0]+lsArr[i-1,0]))/2)
##    ws.append((lsArr[-1,0]+30)-(lsArr[-1,0]+lsArr[-2,0])/2)
##
##    dAvg = sum(np.array(ws)*lsArr[:,1])/sum(ws)

    ret = ls[0][1]
    if len(ls)>1 :
        ws = []
        ws.append((ls[0][0]+ls[1][0])/2 - ls[0][0]+30)
        for i in range(1,len(ls)-1) :
            ws.append(((ls[i][0]+ls[i+1][0]) - (ls[i][0]+ls[i-1][0]))/2)
        ws.append((ls[-1][0]+30)-(ls[-1][0]+ls[-2][0])/2)

        day = [ws[x]*ls[x][1] for x in range(len(ls))]
        ret = sum(day)/sum(ws)
    
    return ret


src = sys.argv[1]
dest = sys.argv[2]

cols = ['Lat','Lon','Ele']+['YR--MODAHRMN','DIR','SPD','GUS','TEMP','ALT']

with open(src) as f:
    contentI = f.readlines()

##contentI = pd.read_csv(src)
##content = contentI.as_matrix().astype('str').tolist()

data = []


content = [contentI[x].split(',') for x in range(len(contentI))]

ofs = 0
lofs = 1

loc = content[lofs][(1-ofs):(3-ofs)]
##print(content[0][(4-ofs)])
d = content[lofs][(4-ofs)]
temp = []
temp.append(content[lofs][(4-ofs):(10-ofs)])
i=lofs+1
while (i < len(content)) :
    if content[i][(1-ofs):(3-ofs)]==loc and content[i][(4-ofs)][0:8]==d[0:8]:
        temp.append(content[i][(4-ofs):(10-ofs)])
        i+=1
    elif len(temp)>0 :
        eph = loc+[d[0:8]]
        
        for j in range(len(temp)) :
##            print(temp[j][0]+'|||')
##            print(temp[j][0][8:10]+'---')
##            print(temp[j][0][10:12]+'---')
            temp[j][0] = float(temp[j][0][8:10])*60+float(temp[j][0][10:12])
        evan = [[temp[x][0],temp[x][1],temp[x][2]] for x in range(len(temp))]
        dels = []
        for j in range(len(evan)) :
            if '*' in evan[j][2] :
                dels.append(j)
        dels.reverse()
        for j in dels :
            del evan[j]
        for j in range(len(evan)) :
            if evan[j][2] == '0' :
                evan[j][1] = '0'
        angs = np.pi/180*np.array([float(evan[x][1]) for x in range(len(evan))])
        vecs = []
        for j in range(len(evan)) :
            vecs.append(float(evan[j][2])*np.array([np.sin(angs[j]),np.cos(angs[j])]))
        nEvan = [[evan[x][0],vecs[x]] for x in range(len(evan))]
        if len(nEvan) > 0 :
            avgWD = timeAvg([[evan[x][0],vecs[x]] for x in range(len(evan))])
##            print(str(avgWD[0])+','+str(avgWD[1]))
    ##        eph.append(avgWD) # no unpack
            # unpack vector
            nAng = np.arctan(avgWD[0]/avgWD[1])
            if avgWD[1] < 0 :
                nAng += np.pi
            eph.append(nAng)
            eph.append(np.linalg.norm(avgWD))
        else :
            eph.append('***')
            eph.append('***')

        for j in range(3,6) :
            evan = [[temp[x][0],temp[x][j]] for x in range(len(temp))]
            dels = []
            for k in range(len(evan)) :
                if '*' in evan[k][1]:
                    dels.append(k)
            dels.reverse()
            for k in dels :
                del evan[k]
            if len(evan)>0 :
                evan2 = [[evan[x][0],float(evan[x][1])] for x in range(len(evan))]
                eph.append(timeAvg(evan2))
            else :
                eph.append('***')

        data.append(eph)
        
        
        loc = content[i][(1-ofs):(3-ofs)]
        d = content[i][(4-ofs)]
        temp = []
        temp.append(content[i][(4-ofs):(10-ofs)])
        i+=1
    else :
        print('DaFuq?')
        i+=1

f = open(dest,'w')

for i in range(len(data)) :
    f.write(data[i][0])
    for j in range(1,len(data[i])) :
        f.write(','+str(data[i][j]))
    f.write('\n')

f.close()
    

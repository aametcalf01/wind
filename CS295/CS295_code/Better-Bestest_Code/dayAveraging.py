import os
import sys
import numpy as np

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

#cols = ['Lat','Lon','Ele']+['YR--MODAHRMN','DIR','SPD','GUS','TEMP','ALT']

with open(src) as f:
    contentI = f.readlines()

data = []


content = [contentI[x].split(',') for x in range(len(contentI))]

loc = content[1][1:3]
d = content[1][4]
temp = []
temp.append(content[1][4:10])
i=2
while (i < len(content)) :
    if content[i][1:3]==loc and content[i][4][0:8]==d[0:8]:
        temp.append(content[i][4:10])
        i+=1
    elif len(temp)>0 :
        eph = loc+[d[0:8]]
        
        for j in range(len(temp)) :
            print(temp[j][0]+'|||')
            print(temp[j][0][8:10]+'---')
            print(temp[j][0][10:12]+'---')
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
        avgWD = timeAvg([[evan[x][0],vecs[x]] for x in range(len(evan))])
        # unpack vector
        eph.append(avgWD)

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
        
        
        loc = content[i][1:3]
        d = content[i][4]
        temp = []
        temp.append(content[i][5:9])
        i+=1
    else :
        print('DaFuq?')
        i+=1

# WRITE DATA
    

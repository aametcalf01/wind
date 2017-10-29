def getLatLonElev():
	"""
	This function creates and returns a dictionary that is keyed by station number 
	(USAF#-WBAN#) and has latitude, longitude, elevation, and begin and end time 
	 stored in a tuple.
	"""
	dic ={}
	f = open("/users/a/a/aametcal/CS295/readmeDocs/isd-history.csv")
	counter = 0;
	for line in f:
		lst = line.split(',')
		#get rid of the newline character and remove the quotations
		for i in range(len(lst)):
			lst[i] = lst[i].strip().strip('"')
		code = lst[0]+"-"+lst[1] #create the USAF#-WBAN# code
		if counter !=0:
			dic[code] =(lst[6],lst[7],lst[8],lst[9],lst[10])	
		counter+=1
	f.close()
	return dic

dic = getLatLonElev()

# clean the dictionary to include only those stations that have latitude, longitude, elevation
# and start and stop times
flag = 0
for station in dic.keys():
	for i in dic[station]:
		if i == '':
			flag+=1
	if flag !=0:
		dic.pop(station)
	flag = 0


f = open('stationInfo.txt','w')

for station in dic.keys():
	tup = dic[station]
	f.write(station+","+tup[0]+","+tup[1]+","+tup[2]+","+tup[3]+","+tup[4]+"\n")
f.close

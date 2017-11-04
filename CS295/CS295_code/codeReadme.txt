dataPreProc.py: 

#this code takes as system arguments: year, file destination and file name, lower lattitude, upper lattitude, western longitude, easter longitude

#Returns a .csv file with all of the specified columns for the specified region for one year


dataPreProc.py:
#this code takes as system arguments: file destination path(don't include the filename), lower lattitude, upper lattitude, western longitude, easter longitude

#Returns a .csv file with all of the specified columns for the specified region for every year in the database where we have full coverage

statByYear.py:
statByYear collects all of the data for a specific station and puts it, chronologically, in one file.  Input structure is python statByYear.py USAF#-WBAN# saveFileName

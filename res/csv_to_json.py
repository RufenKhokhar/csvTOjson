# this is the core libs and core concept for converting csv files to json
# first import libraries for csv and json files
import csv
import json

# input file path
csvFilePath = "deaths.csv"
# output file path
jsonFilePath = "result.json"
# temp. storage Area
data = {}
# opening input file in Reading state
csvFile = open(csvFilePath, 'r')
# opening output file writing state
jsonFile = open(jsonFilePath, 'w')
# reading csv data using csv lib that we imported above
csvFileData = csv.DictReader(csvFile)

# csvRow is storing data using HashTables OR
# Key value pair you can access data uing the headers keys
# if you don't know about csv file formate
# i tell you in short the first line in csv file are the keys and remaning are the values that are seprated by commas(,).
# now just read the values and store in data set using for loops
for csvRow in csvFileData:
    latId = csvRow["Lat"]
    longId = csvRow["Long"]
    data[latId + "," + longId] = csvRow

# now store OR write data into json file using json.dumps function
jsonFile.write(json.dumps(data))
# close opened files
csvFile.close()
jsonFile.close()
# and print msg
print("file converted!")

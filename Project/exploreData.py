import xlrd
from statistics import median

dataLocation = "./Data/dataGathering/tokenizedData.xlsx"

tokenBook = xlrd.open_workbook(dataLocation)
tokenSheet = tokenBook.sheet_by_index(0)

data = []
labels = []

for index in range(1,tokenSheet.nrows):
    data.append(tokenSheet.cell_value(index, 2))
    labels.append(tokenSheet.cell_value(index, 3))

nListData, lListData, oListData = [], [], []

for labelIndex in range(0, len(labels)):
    if(labels[labelIndex] == "n"):
        nListData.append(data[labelIndex])
    elif(labels[labelIndex] == "l"):
        lListData.append(data[labelIndex])
    elif(labels[labelIndex] == "o"):
        oListData.append(data[labelIndex])

print("----------------------")
print("Label frequency values")
print("n - ", len(nListData))
print("l - ", len(lListData))
print("o - ", len(oListData))
print("----------------------")

print("Data which belongs to each label")
print("n - ", nListData)
print("l - ", lListData)
print("o - ", oListData)
print("----------------------")

nUniqueData, lUniqueData, oUniqueData = {}, {}, {}

def getUniqueTokens(dataList, uniqueList):
    for word in dataList:
        if(word not in uniqueList):
            uniqueList[word] = 1
        else:
            uniqueList[word] += 1

getUniqueTokens(nListData, nUniqueData)
getUniqueTokens(lListData, lUniqueData)
getUniqueTokens(oListData, oUniqueData)

print("----------------------")
print("n - ", nUniqueData)
print("l - ", lUniqueData)
print("o - ", oUniqueData)
print("----------------------")

def getAllValues(dictionary):
    for word in dictionary:
        print(dictionary[word])

#print("--------------")
#getAllValues(oUniqueData)
#print("--------------")

def getMinimum(dictionary):
    minimum = 100
    for word in dictionary:
        if(dictionary[word] < minimum):
            minimum = dictionary[word]
    return minimum

def getMaximum(dictionary):
    maximum = 0
    for word in dictionary:
        if(dictionary[word] > maximum):
            maximum = dictionary[word]
    return maximum

def getAverage(dictionary, total):
    return (total / len(dictionary))

def getMedianList(dictionary):
    medianList = []
    for item in dictionary:
        medianList.append(dictionary[item])
    return medianList

def firstQuartile(dictionary):
    print()

def thirdQuartile(dictionary):
    print()

print("----------------------")
print("Number of unique values")
print("n - ", len(nUniqueData))
print("l - ", len(lUniqueData))
print("o - ", len(oUniqueData))
print("----------------------")

print("----------------------")
print("Minimum")
print("n - ", getMinimum(nUniqueData))
print("l - ", getMinimum(lUniqueData))
print("o - ", getMinimum(oUniqueData))
print("----------------------")

print("----------------------")
print("Maximum")
print("n - ", getMaximum(nUniqueData))
print("l - ", getMaximum(lUniqueData))
print("o - ", getMaximum(oUniqueData))
print("----------------------")

print("----------------------")
print("Average")
print("n - ", getAverage(nUniqueData, len(nListData)))
print("l - ", getAverage(lUniqueData, len(lListData)))
print("o - ", getAverage(oUniqueData, len(oListData)))
print("----------------------")

print("----------------------")
print("Median")
print("n - ", median(getMedianList(nUniqueData)))
print("l - ", median(getMedianList(lUniqueData)))
print("o - ", median(getMedianList(oUniqueData)))
print("----------------------")

# Remove all entities that occur only once
def removeOnes(dictionary):
    tempDict = {}
    for word in dictionary:
        if not(dictionary[word] <= 2):
            tempDict[word] = dictionary[word]
    return tempDict

print("----------------------")
nUniqueNew = removeOnes(nUniqueData)
lUniqueNew = removeOnes(lUniqueData)
oUniqueNew = removeOnes(oUniqueData)
#getAllValues(nUniqueNew)

# Count the number of frequencies within the data
def countFrequencies(dictionary):
    tempDictionary = {}
    for word in dictionary:
        if(dictionary[word] not in tempDictionary):
            tempDictionary[dictionary[word]] = 1
        else:
            tempDictionary[dictionary[word]] += 1
    return tempDictionary

#Print in increasing numerical order (from 1 up)
def printOrdered(dictionary):
    for index in sorted(dictionary):
        print(index, ":", dictionary[index], " ")

print("----------------------")
nUniqueFreq = countFrequencies(nUniqueData)
lUniqueFreq = countFrequencies(lUniqueData)
oUniqueFreq = countFrequencies(oUniqueData)
print(nUniqueFreq)
print(lUniqueFreq)
print(oUniqueFreq)

print("----------------------")
printOrdered(oUniqueFreq)

print("----------------------")

uniqueDataOverall = []
for token in data:
    if(token not in uniqueDataOverall):
        uniqueDataOverall.append(token)
print(len(uniqueDataOverall))

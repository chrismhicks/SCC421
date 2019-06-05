import xlrd

dataLocation = "./Data/dataGathering/tokenizedData.xlsx"
reducedDataLocation = "./Data/dataGathering/tokenizedReducedData.xlsx"

tokenBook = xlrd.open_workbook(dataLocation)
tokenSheet = tokenBook.sheet_by_index(0)

reducedBook = xlrd.open_workbook(reducedDataLocation)
reducedSheet = reducedBook.sheet_by_index(0)

def loadData():
    data = []
    labels = []
    for index in range(1,tokenSheet.nrows):
        data.append(tokenSheet.cell_value(index, 2))
        labels.append(tokenSheet.cell_value(index, 3))
    return data, labels

def loadSentenceNumbers():
    sentenceNumbers = []
    for index in range(1, tokenSheet.nrows):
        sentenceNumbers.append(tokenSheet.cell_value(index, 1))
    return sentenceNumbers

def loadCombinedTagsString():
    combinedTags = []
    for index in range(1, tokenSheet.nrows):
        print(tokenSheet.cell_value(index, 6))
        combinedTags.append(tokenSheet.cell_value(index, 6))
    return combinedTags

def loadCombinedTags():
    combinedTags = []
    for index in range(1, tokenSheet.nrows):
        tempCombined = []
        for i in range(0, 6):
            tempCombined.append(tokenSheet.cell_value(index, 7+i))
        combinedTags.append(tempCombined)
    return combinedTags

def loadNumericalTags():
    numericalTags = []
    for index in range(1, tokenSheet.nrows):
        numericalTags.append(tokenSheet.cell_value(index, 5))
    return numericalTags

def getTags(increment):
    tags = []
    for index in range(1, tokenSheet.nrows):
        tags.append(tokenSheet.cell_value(index, 7+increment))
    return tags

#Separate data into specific label types
def separateData(data, labels):
    nList, lList, oList = [], [], []
    for index in range(0, len(labels)):
        if(labels[index] == "n"):
            nList.append(data[index])
        elif(labels[index] == "l"):
            lList.append(data[index])
        elif(labels[index] == "o"):
            oList.append(data[index])
    return nList, lList, oList

# For labels
def oneHotEncode(labels):
    newLabels = [], []

    #n -> 0, l -> 1, o -> 2
    for label in labels:
        if(label == "n"):
            newLabels.append(0)
        elif(label == "l"):
            newLabels.append(1)
        elif(label == "o"):
            newLabels.append(2)
        elif(label == "."):
            newLabels.append(3)
    return newLabels

def loadShortenedData():
    labels, POSTags, tag0, tag1, tag2, tag3, tag4, tag5 = [], [], [], [], [], [], [], []

    for index in range(1, reducedSheet.nrows):
        labels.append(reducedSheet.cell_value(index, 0))
        POSTags.append(reducedSheet.cell_value(index, 1))
        tag0.append(reducedSheet.cell_value(index, 2))
        tag1.append(reducedSheet.cell_value(index, 3))
        tag2.append(reducedSheet.cell_value(index, 4))
        tag3.append(reducedSheet.cell_value(index, 5))
        tag4.append(reducedSheet.cell_value(index, 6))
        tag5.append(reducedSheet.cell_value(index, 7))

    return labels, POSTags, tag0, tag1, tag2, tag3, tag4, tag5
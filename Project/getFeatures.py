import loadData as ld
import nltk
import openpyxl
from openpyxl import Workbook
#nltk.download("averaged_perceptron_tagger")

dataLocation = "./Data/dataGathering/tokenizedData.xlsx"

data, labels = ld.loadData()

# Load data and apply part of speech algorithm to it
def posTagData(data):
    return nltk.pos_tag(data)

posData = posTagData(data)

features = []
for dataEntry in posData:
    features.append(dataEntry[1])

numericalFeatures = []

def convertToNumerical(features):
    for feature in features:
        if(feature == "CC"):
            numericalFeatures.append(1)
        elif(feature == "CD"):
            numericalFeatures.append(2)
        elif (feature == "DT"):
            numericalFeatures.append(3)
        elif (feature == "EX"):
            numericalFeatures.append(4)
        elif (feature == "FW"):
            numericalFeatures.append(5)
        elif (feature == "IN"):
            numericalFeatures.append(6)
        elif (feature == "JJ" or feature == "JJR" or feature == "JJS"):
            numericalFeatures.append(7)
        elif (feature == "LS"):
            numericalFeatures.append(8)
        elif (feature == "MD"):
            numericalFeatures.append(9)
        elif (feature == "NN" or feature == "NNS" or feature == "NNP" or feature == "NNPS"):
            numericalFeatures.append(10)
        elif (feature == "PDT"):
            numericalFeatures.append(11)
        elif (feature == "POS"):
            numericalFeatures.append(12)
        elif (feature == "PRP" or feature == "PRP$"):
            numericalFeatures.append(13)
        elif (feature == "RB" or feature == "RBR" or feature == "RBS"):
            numericalFeatures.append(14)
        elif (feature == "RP"):
            numericalFeatures.append(15)
        elif (feature == "TO"):
            numericalFeatures.append(16)
        elif (feature == "UH"):
            numericalFeatures.append(17)
        elif (feature == "VB" or feature == "VBD" or feature == "VBG" or feature == "VBN" or feature == "VBP" or feature == "VBZ"):
            numericalFeatures.append(18)
        elif (feature == "WDT"):
            numericalFeatures.append(19)
        elif (feature == "WP" or feature == "WP$"):
            numericalFeatures.append(20)
        elif (feature == "WRB"):
            numericalFeatures.append(21)
        else:
            numericalFeatures.append(0)

convertToNumerical(features)


print(features)
print(numericalFeatures)
print("---------------------")

sentenceNumbers = ld.loadSentenceNumbers()

# Get the 3 data entries that are above the current index
# If the sentence number changes, place a 0 instead
def getAbove(index):
    currentSentence = sentenceNumbers[index]
    aboveList = []
    if (index < 9998 and sentenceNumbers[index + 1] == currentSentence):
        aboveList.append(numericalFeatures[index + 1])
    else:
        aboveList.append(0)
    if (index < 9997 and sentenceNumbers[index + 2] == currentSentence):
        aboveList.append(numericalFeatures[index + 2])
    else:
        aboveList.append(0)
    if (index < 9996 and sentenceNumbers[index + 3] == currentSentence):
        aboveList.append(numericalFeatures[index + 3])
    else:
        aboveList.append(0)
    return aboveList

# Get the 3 data entries that are below the current index
# If the sentence number changes, place a 0 instead
def getBelow(index):
    currentSentence = sentenceNumbers[index]
    belowList = []
    if (index > 2 and sentenceNumbers[index - 3] == currentSentence):
        belowList.append(numericalFeatures[index - 3])
    else:
        belowList.append(0)
    if (index > 1 and sentenceNumbers[index - 2] == currentSentence):
        belowList.append(numericalFeatures[index - 2])
    else:
        belowList.append(0)
    if (index > 0 and sentenceNumbers[index - 1] == currentSentence):
        belowList.append(numericalFeatures[index - 1])
    else:
        belowList.append(0)
    return belowList


def createVectors():
    combinedList = []
    for index in range(0, len(features)):
        combinedList.append(getBelow(index) + getAbove(index))
    return combinedList

vectorList = createVectors()

for item in vectorList:
    print(item[5])

#for item in features:
#    print(item)
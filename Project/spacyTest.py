import spacy
import xlrd
import json

# Test to check how well spacy performs with the given data
# Data is manually checked

dataLocation = "./Data/dataGathering/tokenizedData.xlsx"
jsonFileLocation = "./Data/dataGathering/rawData.json"

nlp = spacy.load("en_core_web_sm")

tokenBook = xlrd.open_workbook(dataLocation)
tokenSheet = tokenBook.sheet_by_index(0)

dataList = []

# Load data into a contiguous string
#for index in range(1,tokenSheet.nrows):
#    dataList += tokenSheet.cell_value(index, 2) + " "

with open(jsonFileLocation, "r") as jsonFile:
    for line in jsonFile:
        rawData = json.loads(line)
        for sentence in rawData["Data"][0]["Summary"]:
            dataList.append(sentence)

for sentence in dataList:
    test = nlp(sentence)
    print(sentence)
    for entity in test.ents:
        print(entity.text, entity.label_)
    print("-----------------------")



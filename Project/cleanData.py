import xlrd

dataLocation = "./Data/dataGathering/tokenizedData.xlsx"

tokenBook = xlrd.open_workbook(dataLocation)
tokenSheet = tokenBook.sheet_by_index(0)

# Check for missing or null values value
# Check for incorrect value (must be n, o, l, or .)

totalCounter = 0
incorrectCounter = 0
missingCounter = 0

allowedValues = ["n", "o", "l", "."]

for index in range(1,tokenSheet.nrows):
    totalCounter += 1
    if(tokenSheet.cell_value(index, 3) not in allowedValues):
        incorrectCounter += 1
        print(tokenSheet.cell_value(index, 3))
    if(tokenSheet.cell_value(index, 3) is None):
        missingCounter += 1

print(totalCounter)
print(incorrectCounter)
print(missingCounter)


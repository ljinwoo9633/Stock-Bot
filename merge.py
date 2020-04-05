import csv

resultFile = open('./mergedStock.csv', 'w', encoding='euc-kr', newline='')
fileOne = open('./mergedStock1.csv', 'r', encoding='euc-kr')
fileTwo = open('./mergedStock2.csv', 'r', encoding='euc-kr')

readerOne = csv.reader(fileOne)
readerTwo = csv.reader(fileTwo)

writer = csv.writer(resultFile)

index = 0
for line in readerOne:
    if(index == 0):
        pass
    writer.writerow(line)

index = 0

for line in readerTwo:
    if(index == 0):
        pass
    writer.writerow(line)

fileOne.close()
fileTwo.close()
resultFile.close()
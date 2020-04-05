import csv

f = open('./stockInfo.csv', 'r', encoding='euc-kr')
fileOne = open('./filteredStockInfoOne.csv', 'w', encoding='euc-kr', newline='')

reader = csv.reader(f)
writer = csv.writer(fileOne)

writer.writerow(('Company Name', 'EPS before 4', 'EPS before 3', 'EPS before 2', 'EPS before 1', 'PER before 4', 'PER before 3', 'PER before 2', 'PER before 1', 'ROE before 4', 'ROE before 3', 'ROE before 2', 'ROE before 1', 'RATING_OF_DEBT before 4', 'RATING_OF_DEBT before 3', 'RATING_OF_DEBT before 2', 'RATING_OF_DEBT before 1', 'RATING_OF_MARGIN before 4', 'RATING_OF_MARGIN before 3', 'RATING_OF_MARGIN before 2', 'RATING_OF_MARGIN before 1'))

for line in reader:
    try:
        if ',' in line[1]:
            line[1] = line[1].replace(',', '')
        if ',' in line[2]:
            line[2] = line[2].replace(',', '')
        if ',' in line[3]:
            line[3] = line[3].replace(',', '')

        if int(line[1]) > 0 and int(line[2]) > 0 and int(line[3]) > 0:
            writer.writerow(line)
    except:
        pass

f.close()
fileOne.close()

#for line in reader:
#    try:
#        if(int(line[1]) > 0 and int(line[2]) > 0 and int(line[3]) > 0):
#            writer.writerow(line)
#    except:
#        pass

#f.close()
#fileOne.close()

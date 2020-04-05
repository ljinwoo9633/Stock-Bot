import requests
import csv
from urllib.request import urlopen
from urllib.parse import urlparse, parse_qs, parse_qsl
from bs4 import BeautifulSoup
from selenium import webdriver
import random
import time


def getStockNumbers():
    baseUrl = 'https://finance.naver.com'
    stockUrl = 'https://finance.naver.com/sise/sise_group.nhn?type=upjong'
    stockNumbers = []
    session = requests.Session()
    header = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)\
			AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
			"Accept":"text/html,application/xhtml+xml,application/xml;\
			q=0.9,imgwebp,*/*;q=0.8"
    }
    req = session.get(stockUrl,headers=header)
    bs = BeautifulSoup(req.text, 'html.parser')
    tmps = bs.findAll('a')
    for tmp in tmps:
        if "/sise/sise_group_detail.nhn?type=upjong&no=" in tmp.attrs['href']:
            parts = urlparse(baseUrl + tmp.attrs['href'])
            qs = dict(parse_qsl(parts.query))
            stockNumbers.append(qs['no'])
    
    return stockNumbers




def getStockCodes(stockNumber):
    stockCodes = []
    baseUrl = 'https://finance.naver.com'
    stockNumberUrls = baseUrl + '/sise/sise_group_detail.nhn?type=upjong&no=' + stockNumber

    session = requests.Session()
    header = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)\
			AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
			"Accept":"text/html,application/xhtml+xml,application/xml;\
			q=0.9,imgwebp,*/*;q=0.8"
    }
    req = session.get(stockNumberUrls,headers=header)
    bs = BeautifulSoup(req.text, 'html.parser')
    tmps = bs.findAll('a')
    for tmp in tmps:
        if '/item/main.nhn?code' in tmp.attrs['href']:
            parts = urlparse(baseUrl + tmp.attrs['href'])
            qs = dict(parse_qsl(parts.query))
            stockCodes.append(qs['code'])

    return stockCodes

def getStockInfo(writer, f, stockCode):
    EPS = []
    PER = []
    ROE = []
    RATING_OF_DEBT = []
    RATING_OF_MATRGIN = []
    
    baseUrl = 'https://finance.naver.com/item/main.nhn?code='
    stockUrl = baseUrl + stockCode

    driver = webdriver.Chrome(executable_path='chromedriver.exe')

    driver.get(stockUrl)
    time.sleep(random.randint(7, 10))

    try:
        companyName = driver.find_element_by_xpath('//*[@id="middle"]/div[1]/div[1]/h2/a').text
        driver.implicitly_wait(random.randint(3, 5))
        
        EPS.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[10]/td[1]').text)
        driver.implicitly_wait(random.randint(3, 5))
        EPS.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[10]/td[2]').text)
        driver.implicitly_wait(random.randint(3, 5))
        EPS.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[10]/td[3]').text)
        driver.implicitly_wait(random.randint(3, 5))
        EPS.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[10]/td[4]').text)
        driver.implicitly_wait(random.randint(3, 5))

        PER.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[11]/td[1]').text)
        driver.implicitly_wait(random.randint(3, 5))
        PER.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[11]/td[2]').text)
        driver.implicitly_wait(random.randint(3, 5))
        PER.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[11]/td[3]').text)
        driver.implicitly_wait(random.randint(3, 5))
        PER.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[11]/td[4]').text)
        driver.implicitly_wait(random.randint(3, 5))
        
        ROE.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[6]/td[1]').text)
        driver.implicitly_wait(random.randint(3, 5))
        ROE.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[6]/td[2]').text)
        driver.implicitly_wait(random.randint(3, 5))
        ROE.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[6]/td[3]').text)
        driver.implicitly_wait(random.randint(3, 5))
        ROE.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[6]/td[4]').text)
        driver.implicitly_wait(random.randint(3, 5))
        
        RATING_OF_DEBT.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[7]/td[1]').text)
        driver.implicitly_wait(random.randint(3, 5))
        RATING_OF_DEBT.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[7]/td[2]').text)
        driver.implicitly_wait(random.randint(3, 5))
        RATING_OF_DEBT.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[7]/td[3]').text)
        driver.implicitly_wait(random.randint(3, 5))
        RATING_OF_DEBT.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[7]/td[4]').text)
        driver.implicitly_wait(random.randint(3, 5))
        
        RATING_OF_MATRGIN.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[5]/td[1]').text)
        driver.implicitly_wait(random.randint(3, 5))
        RATING_OF_MATRGIN.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[5]/td[2]').text)
        driver.implicitly_wait(random.randint(3, 5))
        RATING_OF_MATRGIN.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[5]/td[3]').text)
        driver.implicitly_wait(random.randint(3, 5))
        RATING_OF_MATRGIN.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[5]/td[4]').text)
        driver.implicitly_wait(random.randint(3, 5))
        
        writer.writerow((companyName, EPS[0], EPS[1], EPS[2], EPS[3], PER[0], PER[1], PER[2], PER[3], ROE[0], ROE[1], ROE[2], ROE[3], RATING_OF_DEBT[0], RATING_OF_DEBT[1], RATING_OF_DEBT[2], RATING_OF_DEBT[3], RATING_OF_MATRGIN[0], RATING_OF_MATRGIN[1], RATING_OF_MATRGIN[2], RATING_OF_MATRGIN[3]))
        driver.implicitly_wait(random.randint(3, 5))

        driver.close()

    except:
        print("[-]There is no information in this page. Pass this stock information.")
        try:
            companyName = driver.find_element_by_xpath('//*[@id="middle"]/div[1]/div[1]/h2/a').text
            writer.writerow((companyName, "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null"))
            driver.close()
            pass
        except:
            print('[-]Connected Fail... Try it again...')
            
            driver.close()
            time.sleep(random.randint(10, 15))

            driver.get(stockUrl)
            time.sleep(random.randint(7, 10))

            try:
                companyName = driver.find_element_by_xpath('//*[@id="middle"]/div[1]/div[1]/h2/a').text
                driver.implicitly_wait(random.randint(3, 5))
                
                EPS.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[10]/td[1]').text)
                driver.implicitly_wait(random.randint(3, 5))
                EPS.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[10]/td[2]').text)
                driver.implicitly_wait(random.randint(3, 5))
                EPS.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[10]/td[3]').text)
                driver.implicitly_wait(random.randint(3, 5))
                EPS.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[10]/td[4]').text)
                driver.implicitly_wait(random.randint(3, 5))

                PER.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[11]/td[1]').text)
                driver.implicitly_wait(random.randint(3, 5))
                PER.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[11]/td[2]').text)
                driver.implicitly_wait(random.randint(3, 5))
                PER.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[11]/td[3]').text)
                driver.implicitly_wait(random.randint(3, 5))
                PER.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[11]/td[4]').text)
                driver.implicitly_wait(random.randint(3, 5))
                
                ROE.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[6]/td[1]').text)
                driver.implicitly_wait(random.randint(3, 5))
                ROE.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[6]/td[2]').text)
                driver.implicitly_wait(random.randint(3, 5))
                ROE.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[6]/td[3]').text)
                driver.implicitly_wait(random.randint(3, 5))
                ROE.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[6]/td[4]').text)
                driver.implicitly_wait(random.randint(3, 5))
                
                RATING_OF_DEBT.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[7]/td[1]').text)
                driver.implicitly_wait(random.randint(3, 5))
                RATING_OF_DEBT.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[7]/td[2]').text)
                driver.implicitly_wait(random.randint(3, 5))
                RATING_OF_DEBT.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[7]/td[3]').text)
                driver.implicitly_wait(random.randint(3, 5))
                RATING_OF_DEBT.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[7]/td[4]').text)
                driver.implicitly_wait(random.randint(3, 5))
                
                RATING_OF_MATRGIN.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[5]/td[1]').text)
                driver.implicitly_wait(random.randint(3, 5))
                RATING_OF_MATRGIN.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[5]/td[2]').text)
                driver.implicitly_wait(random.randint(3, 5))
                RATING_OF_MATRGIN.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[5]/td[3]').text)
                driver.implicitly_wait(random.randint(3, 5))
                RATING_OF_MATRGIN.append(driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/table/tbody/tr[5]/td[4]').text)
                driver.implicitly_wait(random.randint(3, 5))
                
                writer.writerow((companyName, EPS[0], EPS[1], EPS[2], EPS[3], PER[0], PER[1], PER[2], PER[3], ROE[0], ROE[1], ROE[2], ROE[3], RATING_OF_DEBT[0], RATING_OF_DEBT[1], RATING_OF_DEBT[2], RATING_OF_DEBT[3], RATING_OF_MATRGIN[0], RATING_OF_MATRGIN[1], RATING_OF_MATRGIN[2], RATING_OF_MATRGIN[3]))
                driver.implicitly_wait(random.randint(3, 5))

                driver.close()

            except:
                companyName = driver.find_element_by_xpath('//*[@id="middle"]/div[1]/div[1]/h2/a').text
                driver.implicitly_wait(random.randint(3, 5))
                writer.writerow((companyName, "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null"))
                driver.close()
                pass
            

#stockNumbers = getStockNumbers()
#checkedNumber = ["235", "217", "164", "203", "231", "194", "215", "197", "199", "134", "109", "189", "38", "201", "36", "213", "145", "12", "185", "214", "177", "222", "166", "190", "140", "174", "33", "204", "173", "207", "211", "206", "202", "234", "44", "232", "171", "35", "191", "218", "168", "212", "220"]
#tmpNumbers = []

#for number in checkedNumber:
#    if number in stockNumbers:
#        tmpIndex = stockNumbers.index(number)
#        stockNumbers.pop(tmpIndex)


#print(stockNumbers)

#stockCode를 이용해서 재무정보 뽑아오기
#stockCodes = ["084670", "068400", "024800", "038390"]

#f = open('stockInfo.csv', 'w', encoding='euc-kr', newline='')
#writer = csv.writer(f)
#writer.writerow(('Company Name', 'EPS before 4', 'EPS before 3', 'EPS before 2', 'EPS before 1', 'PER before 4', 'PER before 3', 'PER before 2', 'PER before 1', 'ROE before 4', 'ROE before 3', 'ROE before 2', 'ROE before 1', 'RATING_OF_DEBT before 4', 'RATING_OF_DEBT before 3', 'RATING_OF_DEBT before 2', 'RATING_OF_DEBT before 1', 'RATING_OF_MARGIN before 4', 'RATING_OF_MARGIN before 3', 'RATING_OF_MARGIN before 2', 'RATING_OF_MARGIN before 1'))
#for stockCode in stockCodes:
#    getStockInfo(writer, f, stockCode)
#f.close()

stockNumbers = ["204"]

f = open('stockInfo.csv', 'w', encoding='euc-kr', newline="")
writer = csv.writer(f)
writer.writerow(('Company Name', 'EPS before 4', 'EPS before 3', 'EPS before 2', 'EPS before 1', 'PER before 4', 'PER before 3', 'PER before 2', 'PER before 1', 'ROE before 4', 'ROE before 3', 'ROE before 2', 'ROE before 1', 'RATING_OF_DEBT before 4', 'RATING_OF_DEBT before 3', 'RATING_OF_DEBT before 2', 'RATING_OF_DEBT before 1', 'RATING_OF_MARGIN before 4', 'RATING_OF_MARGIN before 3', 'RATING_OF_MARGIN before 2', 'RATING_OF_MARGIN before 1'))

for stockNumber in stockNumbers:
    stockCodes = getStockCodes(stockNumber)
    for stockCode in stockCodes:
        getStockInfo(writer, f, stockCode)

f.close()
            
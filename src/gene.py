import csv
import random
from datetime import datetime, timedelta

def readData(filename, encoding='utf-8'):
    with open(filename, 'r', newline='', encoding=encoding) as file:
        reader = csv.reader(file)
        headers = next(reader)  # 捨棄首列標題
        data = list(reader)
    return headers, data

def writeData(filename, headers, data, encoding='utf-8'):
    with open(filename, 'w', newline='', encoding=encoding) as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

def generateVirtualData(previousRow, nextRow):
    virtualData = []
    for i in range(3):  # 產生三筆虛擬資料
        virtualRow = []
        for j in range(len(previousRow)):
            if j == 0:  # 日期特別處理
                virtualRow.append((datetime.strptime(previousRow[j], '%Y-%m-%d') + timedelta(days=(i+1))).strftime('%Y-%m-%d'))
            else:
                minVal = min(float(previousRow[j]), float(nextRow[j]))
                maxVal = max(float(previousRow[j]), float(nextRow[j]))
                virtualVal = random.uniform(minVal, maxVal)
                virtualRow.append(round(virtualVal, 2))
        virtualData.append(virtualRow)
    return virtualData

def generateExtendedData(inputFilename, outputFilename):
    headers, data = readData(inputFilename)
    extendedData = []
    for i in range(len(data)-1):
        previousRow = data[i]
        nextRow = data[i+1]
        extendedData.append(previousRow)
        extendedData.extend(generateVirtualData(previousRow, nextRow))
    extendedData.append(data[-1])
    writeData(outputFilename, headers, extendedData)

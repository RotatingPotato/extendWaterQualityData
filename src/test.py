import csv

def readWaterQualityData(filename):
    data = []
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

# 測試讀取數據
waterQualityData = readWaterQualityData('output/data.csv')
print(waterQualityData[0])  # 檢查第一行數據以確認是否包含 "Date" 鍵值對

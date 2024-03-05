import csv
import matplotlib.pyplot as plt

# 讀取水質資料
def readWaterQualityData(filename):
    data = []
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

# 繪製 pH 值折線圖
def plotPH(data):
    dates = [record['Date'] for record in data]
    pH_values = [float(record['pH']) for record in data]
    plt.figure(figsize=(10, 5))
    plt.plot(dates, pH_values, marker='o', linestyle='-')
    plt.title('pH Value Over Time')
    plt.xlabel('Date')
    plt.ylabel('pH')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# 繪製 DO 值折線圖
def plotDO(data):
    dates = [record['Date'] for record in data]
    DO_values = [float(record['DO']) for record in data]
    plt.figure(figsize=(10, 5))
    plt.plot(dates, DO_values, marker='o', linestyle='-')
    plt.title('DO Value Over Time')
    plt.xlabel('Date')
    plt.ylabel('DO')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plotEC(data):
    dates = [record['Date'] for record in data]
    EC_values = [float(record['EC']) for record in data]
    plt.figure(figsize=(10, 5))
    plt.plot(dates, EC_values, marker='o', linestyle='-')
    plt.title('EC Value Over Time')
    plt.xlabel('Date')
    plt.ylabel('EC')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plotORP(data):
    dates = [record['Date'] for record in data]
    ORP_values = [float(record['ORP']) for record in data]
    plt.figure(figsize=(10, 5))
    plt.plot(dates, ORP_values, marker='o', linestyle='-')
    plt.title('ORP Value Over Time')
    plt.xlabel('Date')
    plt.ylabel('ORP')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# 讀取水質資料
waterQualityData = readWaterQualityData('output/data.csv')

# 繪製 折線圖
plotPH(waterQualityData)
plotDO(waterQualityData)
plotEC(waterQualityData)
plotORP(waterQualityData)
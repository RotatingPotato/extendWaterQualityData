from src import gene, plot

def main():
    inputFile = 'input/data.csv'
    outputFile = 'output/data.csv'

    gene.generateExtendedData(inputFile, outputFile)
    plot.plotData(outputFile)

if __name__ == "__main__":
    main()

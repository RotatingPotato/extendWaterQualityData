from src import gene, plot

def main():
    inputFilename = 'input/data.csv'
    outputFilename = 'output/data.csv'

    gene.generateExtendedData(inputFilename, outputFilename)
    plot.plotData(outputFilename)

if __name__ == "__main__":
    main()

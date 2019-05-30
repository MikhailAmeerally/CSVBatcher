import csv
import os

if(not os.path.isdir('chunks')):
    os.mkdir("chunks")

fileToBeRead = 'BookSkusWithBadTags.csv'
stringBuilder = []
skuCount = 0
fileName = 'chunks/bookSkusChunk_'
fileCount = 1
batchSize = 50000
with open(fileToBeRead, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for sku in reader:
        skuCount += 1
        stringBuilder += sku

        if(skuCount > batchSize):
            print("Writing to "+fileName+str(fileCount))
            with open(fileName+str(fileCount)+'.csv', 'w+') as newChunk:
                writer = csv.writer(newChunk, delimiter=',')
                writer.writerow(stringBuilder)
            fileCount +=1
            stringBuilder = []
            skuCount = 0

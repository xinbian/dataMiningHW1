import csv
import numpy as np

with open('iris.data') as csvfile:
    irisData = csv.reader(csvfile, delimiter=',')
    sepLens = []
    sepWids = []
    petLens = []
    petWids = []
    irisClasss = []
    for row in irisData:
       #  sepLen = row[0]
         sepWid = row[1]
         petLen = row[2]
         petWid = row[3]
         irisClass = row[4]
         sepLens.append(sepLen)
         sepWids.append(sepWid)
         petLens.append(petLen)
         petWids.append(petWid)
         irisClasss.append(irisClass)

#convert to numerics
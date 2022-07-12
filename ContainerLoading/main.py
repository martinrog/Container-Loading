#!/usr/bin/env python3
# https://github.com/martinrog/Container-Loading.git
from BinPacker.Packer import Packer
from BinPacker.Container import Container
from BinPacker.Box import Box
import pandas as pd
import time
import json
import matplotlib.pyplot as plt

def addToContainer(name, width, height, dept, weight, quantity):
    """This function can add one or more boxes to the container"""
    for item in range(quantity):
        packer.add_item(Box(name, width, height, dept, weight))
    return width, height, dept, quantity
    
def importCsvContainer(path):
    """This function takes the data from an excel CSV exported file and sends it to another function"""
    data = pd.read_csv(r'{}'.format(path),delimiter=';')
    json_data=json.loads(data.to_json(index=None, orient="table"))

    for row in json_data["data"]:
        packer.add_bin(Container(row['naam'],row['breedte'],row['hoogte'],row['lengte'],row['max_gewicht']))

def importCSV(path):
    """This function takes the data from an excel CSV exported file and sends it to another function"""
    data = pd.read_csv(r'{}'.format(path),delimiter=';')
    json_data=json.loads(data.to_json(index=None, orient="table"))

    for row in json_data["data"]:
        addToContainer(row["naam"],row["breedte"],row["hoogte"],row["lengte"],row["gewicht"],row["hoeveelheid"])
     
def getFitVol(self):
    """Return volume of all fitted boxes"""
    tota = []
    for b in packer.bins:
        for item in b.items:
            tota.append(item.get_volume())
    return sum(tota)

def getUnfitVol(self):
    """Return volume of all unfitted boxes"""
    tota = []
    for b in packer.bins:
        for item in b.unfitted_items:
            tota.append(item.get_volume())
    return sum(tota)

def getTotalWeight(self):
    """Return weight of all fitted boxes"""
    tota = []
    for b in packer.bins:
        for item in b.items:
            tota.append(item.weight)
    return sum(tota)

def getTotalUnpackedWeight(self):
    """Return weight of all unfitted boxes"""
    tota = []
    for b in packer.bins:
        for item in b.unfitted_items:
            tota.append(item.weight)
    return sum(tota)

def plotRuntimeData(path):
    data = pd.read_csv(r'{}'.format(path), delimiter=';')
    json_data = json.loads(data.to_json(index=None, orient="table"))
    xcords = []
    ycords = []

    for row in json_data["data"]:
        xcords.append(row['aantalDozen'])
        ycords.append(row['tijd'])

    plt.scatter(xcords, ycords,s=9)
    plt.ylabel('Run time in seconds')
    plt.xlabel('Total amount of boxes')
    plt.title('Runtime')
    plt.show()

def writeRunData(path,boxTotal):
    with open(path,'a') as file:
        file.write(f'\n{boxTotal};{total_time.__round__(5)}')
        file.close()

if __name__ == '__main__':

    packer = Packer()
    #TIMER
    start = time.time()

    importCsvContainer('Paklijsten/ContainerSize.csv')

    importCSV('Paklijsten/Paklijst17.csv')

    #pack the boxes
    packer.pack()

    boxCountFit = 0
    boxCountUnfit =0

    for b in packer.bins:
        for i in b.items:
            boxCountFit+=1
        for i in b.unfitted_items:
            boxCountUnfit+=1
    boxCount = boxCountFit+boxCountUnfit
	
    #print the output
    for b in packer.bins:
        print(b.string(),"\n")

        print("FITTED ITEMS:")
        for item in b.items:
            print("=> ", item.string())
        print("------------------------------------------------------------")
        print(f"Total packed volume: {getFitVol(packer)}")
        print(f"Total packed weight: {getTotalWeight(packer)}")
        print(f"Total packed boxes: {boxCountFit}")
	
        print("\nUNFITTED ITEMS:")
        for item in b.unfitted_items:
            print("=> ", item.string())
        print("------------------------------------------------------------")
        print(f"Total unpacked volume: {getUnfitVol(packer)}")
        print(f"Total unpacked weight: {getTotalUnpackedWeight(packer)}")
        print(f"Total unpacked boxes: {boxCountUnfit}")

    #END TIMER
    end = time.time()
    total_time = end - start
    print(f"\nRunning time: {total_time.__round__(9)} seconds")
    print(f"Total boxes: {boxCount}")

    writeRunData('runtimeData.csv', boxCount)
    plotRuntimeData('runtimeData.csv')


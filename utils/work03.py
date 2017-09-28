#Work03
#James Smith and Ish Mahdi

import random
global d
d = {}


#CORE FUNCTIONS =============================================================================

#returns a list of the csv file lines.
def open_read(csvFile):
    csv_file = open(csvFile, 'r')
    return csv_file.readlines()[1:len(csv_file.readlines())-1]

def lineToDictEntry(line):
    #This block deals with commas and splicing
    if line.find('''",''') == -1:
        job = line.split(",")[0]
        percentage = line.split(",")[1]
        link = line.split(",")[2]

    else:
        job = line.split('''",''')[0][1:]
        percentage = line.split('''",''')[1].split(",")[0]
        link = line.split('''",''')[1].split(",")[1]
    numLinkTuple = (float(percentage),link)
    d[job] = numLinkTuple
    return d

#Turns the csv line list into a dictionary with Profession:Percentage
def listToDict(lineList):
    #iterate through the list and fill dictionary
    for line in lineList:
        lineToDictEntry(line)

#Picks weighted random key value from dictionary
def getRandom():
    threshold = random.random() * 99.8#total percentage
    counter = 0
    for entry in d:
        counter += d[entry][0]
        if(counter > threshold):
            return entry
#CORE FUNCTIONS ===========================================================================

#testing program
def run(csvFile):
    lineList = open_read(csvFile)
    listToDict(lineList)
    return(d, (getRandom()))

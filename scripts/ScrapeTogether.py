import os
import datetime
import sys




def processing(filename):
    x = []
   
    with open(filename) as logFile:
        for lines in logFile:
            x.append(lines)
    
    return x

def readFirstLine(filename):
    with open(filename) as logFile:
        return logFile.readline()


def getTime(string):
    return string[1:string.find("]")]


def writeList(file, list):
    for line in list:
        file.write(line)

def getLast(file):
    with open(file) as logFile:
        x = logFile.readlines()
    return x[-1]


def main(item_list):
    previous_value = 0
    match = 0
    f = open(directory + "\\match" + str(match) + ".txt", "a")



    for items in item_list:
        

        # try except because i'm to tired to bug fix
        try:
            # gets the current file being used
            current_file = address + items
            # First Value of appending file
            first_value = getTime(readFirstLine(current_file))
            
            #checks if it's time earlier than the previous
            if(float(first_value) >= float(previous_value)):
                writeList(f, processing(current_file))

            # incremants match by one closes last file then writes to a new file
            else:
                match += 1
                f.close()
                f = open(directory + "\\match" + str(match) + ".txt", "a")
                writeList(f, processing(current_file))
                previous_time = 0

            # gets new previous value
            previous_value = getTime(getLast(current_file))
        except:
            pass
    

if __name__ == "__main__":
    path = sys.argv[1]
    print(path)
    itemList = os.listdir(path)
    address = path + '\\'
    directory = address + str(datetime.datetime.now()).replace(":","")
    os.mkdir(directory)
    main(itemList)
       

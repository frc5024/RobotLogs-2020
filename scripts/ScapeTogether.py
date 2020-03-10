import os
import datetime


item_list = os.listdir("C:\\Users\\willm\\Desktop\\Coding\\RobotLogs-2020\\live")
address = 'C:\\Users\\willm\\Desktop\\Coding\\RobotLogs-2020\\live\\'
directory = address + str(datetime.datetime.now()).replace(":","")
os.mkdir(directory)


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
    return string.find("]")


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
        
        # First Value of appending file
        first_value = readFirstLine(address + items)
        
        if(float(first_value) >= float(previous_value)):
            writeList(f, processing(address + items))
        

        # # try:

        # first_time_value = readFirstLine(address + items)
        # last_time_value = getLast(address + items)


        # start_time = float(first_time_value[1:getTime(first_time_value)])
        # end_time = float(last_time_value[1:getTime(last_time_value)])
        
        
        # if(end_time <= previous_time):
        #     writeList(f, processing(address + items))
        #     previous_time = end_time
        # else:
        #     match += 1
        #     f.close()
        #     f = open(directory + "\\match" + str(match) + ".txt", "a")
        #     previous_time = 0
        # # except:
        #     # print("exception")    
        # # print(end_time)
        # # print(f"Current Number {start_time} Previous Time {previous_time}")
        # # print(start_time >= previous_time if "Same File" else "Different File")
    

main(item_list)
       

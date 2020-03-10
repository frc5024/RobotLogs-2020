import os
import datetime


item_list = os.listdir("C:\\Users\\willm\\Desktop\\Coding\\RobotLogs-2020\\live")
address = 'C:\\Users\\willm\\Desktop\\Coding\\RobotLogs-2020\\live\\'
directory = address + str(datetime.datetime.now()).replace(":","")
# os.mkdir(directory)


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


def main(item_list):
    previous_time = 0
    for items in item_list:
        # try:

        first_time_value = readFirstLine(address + items)
        time = first_time_value[1:getTime(first_time_value)]
        
        print(int(time))
        if(time >= 0):
            print("same set")
        # else:
        #     previous_time = 0
        # except:
            
        
    

main(item_list)

#print(processing(address  + 'RobotLog-2020-03-06.18_55_20.txt'))

# for items in item_list:
    
#     if(items[9:13] != "" and  int(items[9:13]) >= 2020):
        
#         print(items)
       

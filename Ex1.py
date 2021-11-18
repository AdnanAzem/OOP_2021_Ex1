import csv
import sys
import subprocess

from building import Building
from call import CallForElevator

def loadFiles():
    global files
    arguments = sys.argv
    try:
        files.append("data\\Ex1_input\\Ex1_Buildings\\" + arguments[1])
        files.append("data\\Ex1_input\\Ex1_Calls\\" + arguments[2])
        files.append("outputs\\" + arguments[3])

    except FileNotFoundError as e:
        print(e)

def loadCalls(file):
    calls
    with open(file, 'r') as f:
        dataFile = csv.reader(f)
        for c in dataFile:
            if isValidCall(c):
                calls.append(CallForElevator(c))

def isValidCall(call):
    building
    src = int(call[2])
    dest = int(call[3])
    if building.maxFloor < src or building.minFloor > src:
        return False
    if building.maxFloor < dest or building.minFloor > dest:
        return False
    return True

def myAlgo():
    global calls
    global building
    elevs = building.elevators
    for c in calls:
        currTime = c.time
        minElev = building.elevators[0]
        for e in elevs:
            e.doneCalls(currTime)
            if minElev.arrivedTime(c) > e.arrivedTime(c):
                minElev = e
        minElev.addCallToList(c)
        c.changeAllocated(minElev, building)
        c.changeTotalTime(currTime+minElev.arrivedTime(c)+minElev.calcTime(c.src,c.dest))

def saveOutput(file):
    global calls
    data = []
    for c in calls:
        v = c.__dict__
        v.popitem()
        data.append(v.values())
    with open(file, 'w', newline='') as f:
        output = csv.writer(f)
        output.writerows(data)

def run(building, output):
    subprocess.Popen(["powershell.exe", "java -jar tester\\Ex1_checker_V1.2_obf.jar 212068597,208940320 " + building + "  " + output + "  " + output + "_tester.log"])


if __name__ == '__main__':
    print("write the directory for json file: ")
    files = [input()]
    print("write the directory for call file: ")
    files.append(input())
    print("write the directory for output file: ")
    files.append(input())

    loadFiles
    building = Building(files[0])
    calls = []
    loadCalls(files[1])
    myAlgo()
    saveOutput(files[2])
    run(files[0], files[2])
    print("Done!")


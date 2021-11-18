from elevator import Elevator
class CallForElevator:
    global LEVEL
    global DONE
    LEVEL = 0
    DONE = 3

    def __init__(self,file):
        self.name = file[0]
        self.time = float(file[1])
        self.src = int(file[2])
        self.dest = int(file[3])
        self.state = int(file[4])
        self.allocatedTo = int(file[5])
        self.totalTime = -1

    def __str__(self):
        return self.name + ", " + str(self.time) + ", " + str(self.src) + ", " + str(self.dest) + ", " + self.state + ", " + self.allocatedTo

    def changeState(self, s):
        if not (s == self.LEVEL or s == self.DONE):
            return
        self.state = s

    def changeTotalTime(self, t):
        self.totalTime = t

    def changeAllocated(self, elev, building):
        inFloor = False
        for e in building.elevators:
            if e.id == elev.id:
                inFloor = True
        if not inFloor:
            return
        self.allocatedTo = elev.id

        

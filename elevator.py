
class Elevator:

    def __init__(self,file):
        self.id = int(file["_id"])
        self.speed = float(file["_speed"])
        self.minFloor = int(file["_minFloor"])
        self.maxFloor = int(file["_maxFloor"])
        self.closeTime = float(file["_closeTime"])
        self.openTime = float(file["_openTime"])
        self.startTime = float(file["_startTime"])
        self.stopTime = float(file["_stopTime"])
        self.listCalls = []
        self.elevPos = 0

    def __str__(self):
        return " Elevator ID: " + str(self.id) + "\n" + "Speed: " + str(self.speed) + " CloseTime: " + str(self.closeTime)\
        + " OpenTime: " + str(self.openTime) + " StartTime: " + str(self.startTime) + " StopTime: " + str(self.stopTime) + "\n"

    def doneCalls(self,time):
        for c in self.listCalls:
            if c.totalTime < time:
                c.changeState(c.DONE)
                self.listCalls.remove(c)
                self.elevPos = c.dest

    def changePosition(self,i):
        if i < self.minFloor or i > self.maxFloor:
            return
        self.elevPos = i

    def calcTime(self, currElevPos, dest) -> float:
        floors = abs(currElevPos - dest)
        totalTime = self.openTime + self.closeTime + self.startTime + self.stopTime
        return floors / self.speed + totalTime

    def arrivedTime(self,call):
        totalTime = 0
        currElevPos = self.elevPos
        for c in self.listCalls:
            totalTime += self.calcTime(currElevPos,c.src)
            currElevPos = c.src
        if len(self.listCalls) != 0:
            totalTime += self.calcTime(currElevPos,self.listCalls[-1].dest)
            currElevPos = self.listCalls[-1].dest
        totalTime += float(self.calcTime(currElevPos,call.src))
        return totalTime

    def addCallToList(self, call):
        self.listCalls.append(call)

    
    

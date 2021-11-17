import json
from elevator import Elevator

class Building:

    def __init__(self,file):
        with open(file, 'r') as f:
            loadFile = json.load(f)
            self.minFloor = int(loadFile["_minFloor"])
            self.maxFloor = int(loadFile["_maxFloor"])
            self.elevators = []
            counter = 0
            for elev in loadFile["_elevators"]:
                self.elevators.append((Elevator(elev,counter)))
                counter += 1

    def __str__(self):
        ans = "[" + str(self.maxFloor) + ", " + str(self.maxFloor) + "]\n"
        for elev in self.elevators:
            ans = ans + elev.__str__()
        return ans

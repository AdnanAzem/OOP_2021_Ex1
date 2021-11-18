# OOP_2021_Ex1
we got input at the begining so i thought that our algorithm well get the building and the calls.
so the algorithm will chek the nearst elevator for each call and then ask the elavotor to go floor of the call and to open the doors then to go to the destantion floor and open the doors.

# Offline_Algo
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

import json
from elevator import Elevator

class Building:

    def __init__(self, min_floor, max_floor, elevators):
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.elevators = elevators

    def loadFromJson(self, file_name):
        with open(file_name, "r") as f:
            building_dict = json.load(f)

            self.min_floor = building_dict["_minFloor"]
            self.max_floor = building_dict["_maxFloor"]
            self.elevators = []

            for elv in building_dict["_elevators"]:
                id = elv["_id"]
                speed = elv["_speed"]
                min_floor = elv["_minFloor"]
                max_floor = elv["_maxFloor"]
                close_time = elv["_closeTime"]
                open_time = elv["_openTime"]
                start_time = elv["_startTime"]
                stop_time = elv["_stopTime"]

                self.elevators.append(Elevator(id, speed, min_floor, max_floor, close_time, open_time, start_time, stop_time))

    def __str__(self) -> str:
        return f"minFloor:{self.min_floor} ,maxFloor:{self.max_floor} ,elevators:{self.elevators}\n"

    def __repr__(self) -> str:
        return self.__str__()

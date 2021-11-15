import json

class Elevator:

    def __init__(self, id, speed, min_floor, max_floor, close_time, open_time, start_time, stop_time):
        self.id = id
        self.speed = speed
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.close_time = close_time
        self.open_time = open_time
        self.start_time = start_time
        self.stop_time = stop_time

    def __str__(self) -> str:
        return f"id:{self.id} ,speed:{self.speed} ,minF:{self.min_floor}" \
               f" ,maxF:{self.max_floor} ,closeT:{self.close_time} " \
               f",openT:{self.open_time} ,startT:{self.start_time} ,stopT:{self.stop_time}\n"

    def __repr__(self) -> str:
        return self.__str__()
    
    

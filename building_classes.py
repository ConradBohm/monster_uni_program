class Building:
    def __init__(self, location):
        self.location = location

class LectureTheatre(Building):
    def __init__(self, location, room):
        super().__init__(location)
        self.room_number = room

class Cafeteria(Building):
    pass

class Halls(Building):
    def __init__(self, location, room, band):
        super().__init__(location)
        self.room_number = room
        self.price_band = band

class StudentUnion(Building):
    pass

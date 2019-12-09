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
    def __init__(self, location, room, band, student):
        super().__init__(location)
        self.room_number = room
        self.price_band = band
        self.living_student = student


class StudentUnion(Building):
    pass


class SpookyWorkshop:
    def __init__(self, subject, teacher, room):
        self.subject = subject
        self.teacher = teacher
        self.student_list = []
        self.room_number = room

    def add_student(self, student):
        self.student_list.append(student)


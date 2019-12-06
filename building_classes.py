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
    def __init__(self, location, room, band, student_id):
        super().__init__(location)
        self.room_number = room
        self.price_band = band
        self.living_student = student_id


class StudentUnion(Building):
    pass


class SpookyWorkshop:
    def __init__(self, subject, teacher_id, room):
        self.subject = subject
        self.teacher = teacher_id
        self.student_list = []
        self.room_number = room

    def add_student(self, student_id):
        self.student_list.append(student_id)


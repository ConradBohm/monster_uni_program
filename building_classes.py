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
        self.theatre = room

    def add_student(self, student):
        self.student_list.append(student)

    def list_of_students(self):
        generated_list = []
        for student in self.student_list:
            generated_list.append(student.name)

        return generated_list


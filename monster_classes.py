class Monster:
    def __init__(self, name, legs, colour):
        self.name = name
        self.skills = []
        self.leg_number = legs
        self.colour = colour

    def add_skill(self, skill):
        self.skills.append(skill)


class Student(Monster):
    def __init__(self, name, legs, colour, student_id, grade):
        super().__init__(name, legs, colour)
        self.id = student_id
        self.grade = grade


class Teacher(Monster):
    def __init__(self, name, legs, colour, teacher_id):
        super().__init__(name, legs, colour)
        self.id = teacher_id



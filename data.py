# sample data for working program
from monster_classes import *
from building_classes import *

# Student Data
j_black = Student('James Black', 2, 'Yellow', '001', 'C')
t_foolery = Student('Tom Foolery', 6, 'Greenish', '002', 'B')
j_mcintyre = Student('Jess McIntyre', 4.5, 'Peach', '003', 'A*')
b_jameson = Student('Beth Jameson', 2, 'Black and Blue', '004', 'A')

stud_list = PeopleList()
stud_list.people_list.append(j_black)
stud_list.people_list.append(t_foolery)
stud_list.people_list.append(j_mcintyre)
stud_list.people_list.append(b_jameson)

# Teacher Data
m_rampling = Teacher('Mandy Rampling', 3.9, 'Orange', '100')
j_johnson = Teacher('Jeremy Johnson', 3, 'White', '101')

teach_list = PeopleList()
teach_list.people_list.append(m_rampling)
teach_list.people_list.append(j_johnson)

# Student Halls Data
room_1 = Halls('Main Campus', 1, 'B', j_mcintyre)
room_2 = Halls('Main Campus', 2, 'B', t_foolery)
room_3 = Halls('Main Campus', 3, 'B', b_jameson)
room_4 = Halls('Main Campus', 4, 'B', j_black)

# Lecture Theatre Building Data
lecture_1 = LectureTheatre('Main Campus', 10)
lecture_2 = LectureTheatre('Main Campus', 20)

# Workshop Data
scaring = SpookyWorkshop('Scaring', j_johnson, lecture_1)
spook_science = SpookyWorkshop('Spook Science', m_rampling, lecture_2)


# This menu function is used frequently, and the data file is imported into every function file, so it was
# easier to put this funtion here than to copy it in every function file.
def menu_input():
    while True:
        try:
            choice = int(input('Pick a number from the menu options: '))
            break
        except ValueError:
            print('\nNot a valid number, try again with a number digit from the menu.')

    return choice
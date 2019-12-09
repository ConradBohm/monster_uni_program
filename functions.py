from data import *
# stud_list = [j_black, j_mcintyre, b_jameson, t_foolery]



def students():
    while True:
        print('\nStudents menu:\n'
              '1 -- View Student Details\n'
              '2 -- View Student List\n'
              '3 -- Add Skill to Student\n'
              '4 -- Add Student\n'
              '5 -- Back to Main Menu\n')

        choice = menu_input()

        if choice == 1:
            view_students()
        elif choice == 2:
            student_list()
        elif choice == 3:
            add_skill()
        elif choice == 4:
            new_student()
        elif choice == 5:
            break
        else:
            print('We don\'t have that many options! Try a number on the menu.')


def view_students():
    found = False
    check = input('Which student do you wish to find details on?: ').lower()
    for student in stud_list.people_list:
        if check in student.name.lower():
            print(f'Name: {student.name}\n'
                  f'No. of Legs: {student.leg_number}\n'
                  f'Colour: {student.colour}\n'
                  f'ID: {student.id}\n'
                  f'Grade: {student.grade}\n'
                  f'Skills: {student.skills}')
            found = True
            break
        else:
            continue

    if not found:
        print('That name wasn\'t in our records! Check your spelling or try a different name.')


def student_list():
    for student in stud_list.people_list:
        print(student.name)


def add_skill():
    found = False
    check = input('Which student do you wish to add a skill for? ').lower()
    skill = input('What is the skill you wish to add? ')
    for student in stud_list.people_list:
        if check in student.name.lower():
            student.add_skill(skill)
            found = True
            break

        else:
            continue

    if not found:
        print('That name wasn\'t in our records! Check your spelling or try a different name.')
    else:
        print('Update made.')


def new_student():
    print('Enter new student data:')
    name = input('Enter in the name of the new student. Capitalise first and last name: ')
    legs = input('How many legs does the new student have? ')
    colour = input('What colour is the new student? ')
    i_d = input('What is the new student\'s id? ')
    grade = input('What grade is the student working at? ')

    print(f'Name: {name}\n'
          f'Legs: {legs}\n'
          f'Colour: {colour}\n'
          f'Student ID: {i_d}\n'
          f'Grade: {grade}')

    if input('Is this data correct? Y/N)').lower() == 'y':
        new_student_obj = Student(name, legs, colour, i_d, grade)
        stud_list.people_list.append(new_student_obj)
        print('Student list updated.')

    else:
        print('Input data removed.')

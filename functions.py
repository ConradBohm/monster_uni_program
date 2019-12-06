from data import *
stud_list = [j_black, j_mcintyre, b_jameson, t_foolery]

def menu_input():
    while True:
        try:
            choice = int(input('Pick a number from the menu options: '))
            break
        except ValueError:
            print('\nNot a valid number, try again with a number digit from the menu.')

    return choice


def students():
    while True:
        print('\nStudents menu:\n'
              '1 -- View Student Details\n'
              '2 -- View Student List\n'
              '3 -- Back to Main Menu\n')

        choice = menu_input()

        if choice == 1:
            view_students()
        elif choice == 2:
            student_list()
        elif choice == 3:
            break
        else:
            print('We don\'t have that many options! Try a number on the menu.')


def view_students():
    found = False
    check = input('Which student do you wish to find details on? Use last name: ').lower()
    for student in stud_list:
        if check in student.name.lower():
            print(f'Name: {student.name}\n'
                  f'No. of Legs: {student.leg_number}\n'
                  f'Colour: {student.colour}\n'
                  f'ID: {student.id}\n'
                  f'Grade: {student.grade}')
            found = True
            break
        else:
            continue

    if not found:
        print('That name wasn\'t in our records! Check your spelling or try a different name.')


def student_list():
    for student in stud_list:
        print(student.name)

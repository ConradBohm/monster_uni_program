from data import *

work_list = [scaring, spook_science]
# stud_list = [j_black, j_mcintyre, b_jameson, t_foolery]


def workshops():
    while True:
        print('\nWorkshop menu:\n'
              '1 -- View Workshop Details\n'
              '2 -- View Workshop List\n'
              '3 -- Add Student to Workshop\n'
              '4 -- Back to Main Menu\n')

        choice = menu_input()

        if choice == 1:
            view_workshop()
        elif choice == 2:
            workshop_list()
        elif choice == 3:
            add_student()
        elif choice == 4:
            break
        else:
            print('We don\'t have that many options! Try a number on the menu.')


def view_workshop():
    found = False
    check = input('Which subject do you wish to find details on?: ').lower()
    for workshop in work_list:
        if check in workshop.subject.lower():
            print(f'Subject: {workshop.subject}\n'
                  f'Teacher: {workshop.teacher.name}\n'
                  f'Room: {workshop.theatre.room_number}\n'
                  f'Students: {workshop.list_of_students()}')
            found = True
            break
        else:
            continue

    if not found:
        print('That name wasn\'t in our records! Check your spelling or try a different workshop.')


def workshop_list():
    for workshop in work_list:
        print(workshop.subject)


def add_student():
    found = False
    check = input('Which workshop do you wish to add a student to? ').lower()
    stud = input('Who is the student you wish to add? ').lower()
    for workshop in work_list:
        if check in workshop.subject.lower():
            for student in stud_list.people_list:
                if stud in student.name.lower():
                    workshop.add_student(student)
                    print('Student added.')
            found = True
            break

        else:
            print('tick')
            continue

    if not found:
        print('That name wasn\'t in our records! Check your spelling or try a different subject.')
    else:
        print('Update made.')


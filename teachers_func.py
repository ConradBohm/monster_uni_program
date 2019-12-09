from data import *
# teach_list = [j_johnson, m_rampling]

def staff():
    while True:
        print('\nTeacher menu:\n'
              '1 -- View Teacher Details\n'
              '2 -- View Teacher List\n'
              '3 -- Add Skill to Teacher\n'
              '4 -- Back to Main Menu\n')

        choice = menu_input()

        if choice == 1:
            view_teacher()
        elif choice == 2:
            teacher_list()
        elif choice == 3:
            add_skill()
        elif choice == 4:
            break
        else:
            print('We don\'t have that many options! Try a number on the menu.')


def view_teacher():
    found = False
    check = input('Which teacher do you wish to find details on?: ').lower()
    for teacher in teach_list.people_list:
        if check in teacher.name.lower():
            print(f'Name: {teacher.name}\n'
                  f'No. of Legs: {teacher.leg_number}\n'
                  f'Colour: {teacher.colour}\n'
                  f'ID: {teacher.id}\n'
                  f'Skills: {teacher.skills}')
            found = True
            break
        else:
            continue

    if not found:
        print('That name wasn\'t in our records! Check your spelling or try a different name.')


def teacher_list():
    for teacher in teach_list.people_list:
        print(teacher.name)


def add_skill():
    found = False
    check = input('Which teacher do you wish to add a skill for? ').lower()
    skill = input('What is the skill you wish to add? ')
    for teacher in teach_list.people_list:
        if check in teacher.name.lower():
            teacher.add_skill(skill)
            found = True
            break

        else:
            continue

    if not found:
        print('That name wasn\'t in our records! Check your spelling or try a different name.')
    else:
        print('Update made.')



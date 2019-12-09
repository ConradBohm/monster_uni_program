from functions import *
from teachers_func import *
from workshop_func import *
from room_func import *


print('---///--- Monster University Program ---\\\\\\---\n\n')

# Main loop of the program. Contains the base menu and exit functionality
while True:
    print('1 -- Students\n'
          '2 -- Rooms\n'
          '3 -- Workshops\n'
          '4 -- Staff\n'
          '5 -- Exit\n')

    # Error handling, make sure user enters a number
    choice = menu_input()

    # Numbers relate to the menu options. Functions called are sub-menus
    if choice == 1:
        pass
        students()
    elif choice == 2:
        print('Not in operation yet.')
#        rooms()
    elif choice == 3:
        workshops()
    elif choice == 4:
        staff()
    elif choice == 5:
        print('Thank you for using this program!')
        break
    # Else to return to the top of the loop if user didn't use a number 1-5
    else:
        print('We don\'t have that many options! Try a number on the menu.')

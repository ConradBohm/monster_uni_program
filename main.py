from functions import *

print('---///--- Monster University Program ---\\\\\\---\n\n')
while True:
    print('1 -- Students\n'
          '2 -- Rooms\n'
          '3 -- Workshops\n'
          '4 -- Staff\n'
          '5 -- Exit\n')
    while True:
        try:
            choice = int(input('Pick a number from the menu options: '))
            break
        except ValueError:
            print('\nNot a valid number, try again with a number digit from the menu.')

    if choice == 1:
        pass
#        students()
    elif choice == 2:
        pass
#        rooms()
    elif choice == 3:
        pass
#        workshops()
    elif choice == 4:
        pass
#        staff()
    elif choice == 5:
#        finish()
        break
    else:
        print('We don\'t have that many options! Try a number on the menu.')
from colorama import Fore, Back, Style

print(Fore.YELLOW + "Do you want to join my game? (y | n)")
a = input()
if a == 'y':
    print(Fore.RED + 'Welcome to my game.')
    print(Back.BLUE + 'Which direction you want to go? ( e | s | w | n ')
    print(Style.RESET_ALL)
    di = input()
    if di == 'e':
        print('You walk into post office')
    elif di == 's':
        print('You go to the airport')
    elif di == 'w':
        print('You go home')
    elif di == 'n':
        print('You go shopping')
    else:
        print('You choose a wrong direction')
else:
    print('see you next time')
from colorama import Fore, Back, Style
player_name = "Anonymous"
player_energy = 100
player_money = 0
player_weapon = []



def go_to_forest():
    print(Fore.WHITE + "You jump into the muddy forest. It seems so foggy. You felt a little scare about this new world.")

def go_to_market():
    print(Fore.WHITE + "You have entered the most busy market in our world. You see people are chatting and laughing.")
    print(Fore.WHITE + "A beautiful girl is walking to you. She is asking if you want to buy something.")
    print(Fore.GREEN + "1) Axe $10")
    print(Fore.GREEN + "2) Arrow $20")
    print(Fore.GREEN + "3) Shield $20")
    print(Fore.BLUE + "Choose what you want to buy. Type 0 to go back to hallway.")
    product = input()
    if product == "1":
        go_to_market()
    elif product == "2":
        go_to_market()
    else:
        choose_options()

def choose_options():
    print(Fore.WHITE + "You are standing in the hallway and looking at a mysterious wall which has some ancient words.")
    print(Fore.BLUE + "Tell me where do you want to go \n 1) Market \n 2) Enter the forest \n Type 1 or 2 to choose your option")
    option = input()
    if option == "1":
        go_to_market()
    elif option == "2":
        go_to_forest()

def welcome():
    print(Fore.GREEN + "Welcome to join my PYTHON game")
    print(Fore.BLUE + "Please tell me a nick name:")
    player_name = input()
    if len(player_name) >= 0:
        print(Fore.WHITE + "Hello, %s. It is nice to see you in our PYTHON world!" % player_name)
        choose_options()

def start_game():
    welcome()

start_game()

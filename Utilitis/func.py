from colorama import Fore
from colorama import Style

def success_finish(x):
    print(Fore.LIGHTGREEN_EX+f"{x} Test Finish!"+Style.RESET_ALL)
def printing(x,y):
    if y == "green":
        print(Fore.LIGHTGREEN_EX+x+Style.RESET_ALL)
    elif y == "blue":
        print(Fore.LIGHTBLUE_EX+x+Style.RESET_ALL)
    elif y == "yellow":
        print(Fore.LIGHTYELLOW_EX+x+Style.RESET_ALL)
    elif y == "black":
        print(Fore.LIGHTBLACK_EX+x+Style.RESET_ALL)


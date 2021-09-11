from colorama import init, Fore
import pycenter
init()



def nitrologo():
    nitrologo = Fore.MAGENTA + open('data/nitrologo.txt', 'r', encoding="utf8").read() + Fore.RESET
    print(pycenter.center(nitrologo))


nitrologo()
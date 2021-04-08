import os
import SimpleAuthLib
import time
def menu():
    print('Welcome thanks for using our software')
    input()

def login():
    LicenceKeyForThisSoftware = input('Please give me your licence: ')
    if(SimpleAuthLib.Auth('https://jefff-crack.firebaseio.com/.json', LicenceKeyForThisSoftware)):
        os.system('cls')
        menu()
    else:
        os.system('cls')
        print('Wrong licence for your pc')
        time.sleep(2)
        os.system('cls')
        login()

login()

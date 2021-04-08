#import every dependency that we need
import os
import SimpleAuthLib
import time
#import every dependency that we need

#create menu
def menu():
    print('Welcome thanks for using our software')
    input()
#create menu

#create login function using SimpleAuthLib
def login():
    LicenceKeyForThisSoftware = input('Please give me your licence: ')
    if(SimpleAuthLib.Auth('https://my-python-project-b36f8-default-rtdb.firebaseio.com/.json', LicenceKeyForThisSoftware)):
        os.system('cls')
        menu()
    else:
        os.system('cls')
        print('Wrong licence for your pc')
        time.sleep(2)
        os.system('cls')
        login()
#create login function using SimpleAuthLib

#Executing login function on code start
login()
#Executing login function on code start

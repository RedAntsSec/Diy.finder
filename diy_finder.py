import requests
import random
import os
import time
from colorama import init



def logo():
    
    init()  #for start the colors in windows
    if os.name == 'nt':
        os.system('cls')  #clear console
    else:
        os.system('clear')#clear console
    colors = ['92','93','91','94','95']
    rand = random.choice(colors)  #random the colors
    print ('\033['+rand+'m')
    print ("""
 ____  _         _____ _           _
|  _ \(_)_   _  |  ___(_)_ __   __| | ___ _ __
| | | | | | | | | |_  | | '_ \ / _` |/ _ \ '__|
| |_| | | |_| | |  _| | | | | | (_| |  __/ |
|____/|_|\__, | |_|   |_|_| |_|\__,_|\___|_|
         |___/

    """)
    print ('@RedAntsSec  (Github/Telegram)')
    print ('\nCreated By j0hn for RED ANTS TEAM\n\nWE ARE IRANIAN HACKERS!\n')




def finder():

    di = open(dic, 'r')  #open directory file
    for d in di.readlines():
        
        try:
            d = d.replace('\n', '')
            url = target + d
            r = requests.get(url)
        except KeyboardInterrupt:
            print('\n\033[91mUser Using CTRL-C ...')
            time.sleep(2)  #sleep 2 second 
            print('\n\033[91mExiting ... ')
            time.sleep(2)  #sleep 2 second 
            exit()
        except:
            print ('\033[91m[-] Site Not Found [-]')
            exit()
        if r.status_code == 200:
            print ('\n\033[92m[+] Directory of Target Found : %s' % url)
        
        else:
            print ('\n\033[91m[*] Not Found : %s ' % url)








def main():
    global target
    global dic
    init()
    logo()

    try:
        
        target = str(input('Enter Target with http-> '))
        dic    = str(input('Enter Dictionary File -> '))
    except KeyboardInterrupt:
        print('\033[91mUser Using CTRL-C ...')
        time.sleep(2)
        print('\033[91mExiting ... ')
        time.sleep(2)
        exit()
    if dic == '':
        print ('\033[91mNo File Found\nExiting ...')
        time.sleep(2)
        exit()
    else:
        pass

    finder()
while True:
    main()
    i = str(input('\033[93m[~] Do You Want To Continue yes or no [y or n] -> '))
    if i == 'y' or i == 'Y':
        main()
    if i == 'n' or i == 'N':
        print ('\033[31mExiting...')
        time.sleep(2)
        exit()
    else:
        print ('\033[31mExiting...')
        time.sleep(2)
        exit()

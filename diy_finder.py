import requests
import pyfiglet
import random
import os
import time


def logo():
    os.system('cls' or 'clear')
    colors = ['92','93','91','94','95']
    logo = pyfiglet.figlet_format('Diy Finder')
    rand = random.choice(colors)
    print ('\033['+rand+'m'+logo)
    print ('\nCreated By j0hn for RED ANTS TEAM\nWE ARE IRANIAN HACKERS!\n')



def finder():

    di = open(dic, 'r')
    for d in di.readlines():
        
        try:
            d = d.replace('\n', '')
            url = target + d
            r = requests.get(url)
        except KeyboardInterrupt:
            print('\033[91mUser Using CTRL-C ...')
            time.sleep(2)
            print('\033[91mExiting ... ')
            time.sleep(2)
            exit()
        except:
            print ('\033[91m[-] Site Not Found [-]')
            exit()
        if r.status_code == 200:
            print ('\n\033[92m[+] Directory of Target Found : %s' % url)
            
        else:
            print ('\n\033[91m[*] Not Found : %s ' % url)



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
    print ('\033[91mFile Not Found\nExiting ...')
    time.sleep(2)
    exit()
else:
    pass
finder()

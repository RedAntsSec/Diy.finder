import requests
import random
import os
from time import sleep
from colorama import init
from sys import argv


def logo():
    
    init()  #for start the colors in cmd of windows
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

v1.0.3
    """)
    print ('@RedAntsS3c  (Github/Telegram)')
    print ('\nCreated By j0hn for RED ANTS TEAM\n\nWE ARE IRANIAN!\n')



def finder():
    try:
        di = open(dic, 'r')  #open directory file
    except:
        print("\033[91m[-] File Not Found :( ")
        exit()
    for d in di.readlines():
        
        try:
            d = d.replace('\n', '')
            url = target + d
            
            try:
                if proxy != "":
                    prox_conf = {protocol:proxy}
                    url = "http://" + url
                    r = requests.get(url, proxies=prox_conf)
                else:
                    url = "http://" + url
                    r = requests.get(url) #send a request to url with http
            except:
                if proxy != "":
                    prox_conf = {protocol:proxy}
                    url = "https://" + url
                    r = requests.get(url, proxies=prox_conf)
                else:
                    url = "https://" + url
                    r = requests.get(url) #send a request to url with https
        except KeyboardInterrupt:
            print('\n\033[91mUser Using CTRL-C ...')
            sleep(2)  #sleep 2 second 
            print('\n\033[91mExiting ... ')
            sleep(2)  #sleep 2 second 
            exit()
        except:
            print ('\033[91m[-] Site Not Found [-]')
            exit()
        if r.status_code == 200:
            print ('\n\033[92m[+] Directory of Target Found : %s' % url)
            success = open("Success.txt","a")
            success.write(url + "\n") #write success urls in file
            success.close() #close the file
        else:
            print ('\n\033[91m[i] Not Found : %s ' % url)








def main():
    global target
    global dic
    global proxy
    global protocol
    init()
    logo()
    try:
        try:
            target = argv[1]
            try:
                dic = argv[2] 
            except:
                dic = "path.txt"
            try:
                proxy = argv[3]
            except:
                proxy = ""
            try:
                protocol = argv[4]
            except:
                protocol = ""
        except:
            
            print ("\033[93m\nUsage: python "+argv[0]+" example.com path.txt proxy protocol_of_proxy")
            exit()
            if "http://" in target or "https://" in target:
                target = target.replace("http://","")
                target = target.replace("https://","")
                if target[-1] == "/":
                    target = target.replace("/","")
                    print ("[ ~ ] Your Target: " + target)
            
    except KeyboardInterrupt:
        print('\033[91mUser Using CTRL-C ...')
        sleep(2)
        print('\033[91mExiting ... ')
        sleep(2)
        exit()
    if dic == '':
        print ('\033[91mNo File Found\nExiting ...')
        sleep(2)
        exit()
    else:
        pass

    finder()
while True:
    main()
    i = str(input('\033[93m\n[~] Do You Want To Continue? [Y/n] -> '))
    if i == 'y' or i == 'Y':
        main()
    if i == 'n' or i == 'N':
        print ('\033[31mExiting...')
        sleep(2)
        exit()
    else:
        print ('\033[31mExiting...')
        sleep(2)
        exit()

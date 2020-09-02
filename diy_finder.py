import requests
import random
import os
from time import sleep
from colorama import init
#from sys import argv
import argparse


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
                    r = requests.get(url, proxies=prox_conf)

                else:
                    r = requests.get(url) #send a request to url with http
            
            except:
                if proxy != "":
                    prox_conf = {protocol:proxy}
                    r = requests.get(url, proxies=prox_conf)
                else:
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
        if r.status_code == 200 or r.status_code == 403:
            print ('\n\033[92m[+] Directory of Target Found : %s [%s]' %(url,r.status_code))
            success = open("Success.txt","a")
            success.write(url + "\n") #write success urls in file
            success.close() #close the file
        else:
            print ('\n\033[91m[i] Not Found : %s [%s] ' % (url,r.status_code))








def main():
    global target
    global dic
    global proxy
    global protocol
    init()
    logo()
    parser = argparse.ArgumentParser(description='Usage:')
    parser.add_argument('--target',type=str,required=True)
    parser.add_argument('--dictionary', type=str,default="path.txt")
    parser.add_argument('--proxy' ,type=str)
    parser.add_argument('--protocol',type=str,default="http://")
    args = parser.parse_args()
    
    target = args.target
    dic = args.dictionary
    proxy = args.proxy
    protocol = args.protocol

    if "http://" in target or "https://" in target and target[-1] == "/":
        pass
    else:
        target = protocol+target+"/"

    finder()
if '__main__' in __name__:
    main()

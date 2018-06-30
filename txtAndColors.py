#!/usr/bin/env python
# -*- coding: utf-8 -*-


VERSION = 1.1

def ask(msg):
    return "\033[1m " + msg + "\033[0m"

def notice(msg):
    return "\n\033[1m " + msg + "\033[0m"

def critical(msg):
    return "\n\033[91m " + msg + "\033[0m"

def warning(msg):
    return "\033[93m " + msg + "\033[0m"

def info(msg):
    return "\033[0m " + msg + "\033[0m"

def vulnerable(msg):
    return "\033[91m" + msg + "\033[0m"

def display(msg):
    return "\033[0m " + msg + "\033[0m"


def banner():

    banner = """ 

 _   .-')    _   .-')      .-')                ('-.         .-') _  
( '.( OO )_ ( '.( OO )_   ( OO ).             ( OO ).-.    ( OO ) ) 
 ,--.   ,--.),--.   ,--.)(_)---\_)   .-----.  / . --. /,--./ ,--,'  
 |   `.'   | |   `.'   | /    _ |   '  .--./  | \-.  \ |   \ |  |\  
 |         | |         | \  :` `.   |  |('-..-'-'  |  ||    \|  | ) 
 |  |'.'|  | |  |'.'|  |  '..`''.) /_) |OO  )\| |_.'  ||  .     |/  
 |  |   |  | |  |   |  | .-._)   \ ||  |`-'|  |  .-.  ||  |\    |   
 |  |   |  | |  |   |  | \       /(_'  '--'\  |  | |  ||  | \   |   
 `--'   `--' `--'   `--'  `-----'    `-----'  `--' `--'`--'  `--'   

                                                                    
    by: Aiac0sZ
     
 """ + str(VERSION)
    return banner

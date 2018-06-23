#!/usr/bin/env python
# -*- coding: utf-8 -*-


from core.cofe import *
from txtAndColors import banner, critical
import requests
import argparse
import urllib3


if __name__ == '__main__':
    print(critical(banner()))
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", action="store", dest="url", help="MMPublish URL")
    parser.add_argument("--threads", action="store", dest="max_threads", default=1, help="Number of threads to use")
    parser.add_argument('--random-agent', action ='store_const', const='random_agent', dest='random_agent', default=False, help="Random User-Agent")
    results = parser.parse_args()


    if results.url != None:
        urllib3.disable_warnings()
        mmObj = Cofe(results.url, results.max_threads, results.random_agent)
        mmObj.RandomAgent()
        mmObj.CleanUrl()
        mmObj.ToString()
        mmObj.IsUpOrDown()
        mmObj.IsRobots()
        mmObj.HaveDWR()
        mmObj.GetAdminLogin()
        mmObj.SearchDWRScripts()
        mmObj.xpltUserEmail()
        #mmObj.XptGetURemainder()
        mmObj.XptGetUsersLogin()

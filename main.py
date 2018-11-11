#!/usr/bin/python
# -*- coding: utf-8 -*-

from string import ascii_uppercase as upp
from string import ascii_lowercase as low
from random import SystemRandom
from getpass import getpass
from hashlib import sha256
from os.path import isfile
from string import digits
from os import getcwd

def pass_input(message=""):
    plain = getpass(message).encode('utf-8')
    plain = sha256(plain).hexdigest()
    return plain

choice = SystemRandom().choice

class PasswordGenerator():
    def __init__(self, security=2):
        self.security = security
        self.setsettings()

    def setsettings(self):
        chars = digits; size = 12
        if self.security > 1: chars += upp
        if self.security > 2: chars += low
        if self.security > 3: size = 15

        self.chars = chars
        self.size = size

    def generate_password(self):
        return ''.join(choice(self.chars) for x in range(self.size))

    def savepass(self):
        site = raw_input("Save password for: ")
        new_pass = self.generate_password()
        print("Your new password for %s is '%s'.\n" %(site, new_pass))
        with open('mypass.txt','a') as f:
            f.write(site+"-"+new_pass+"\n")

    def getpass(self):
        mypasses = self.getallpasses()
        site = raw_input("Get password for: ")
        passf = mypasses.get(site)
        if passf is None: print("No password for '%s'.\n" %site)
        else: print("Your password for '%s' is '%s'.\n" %(site, passf))

    def getallpasses(self):
        mypasses = {}
        with open('mypass.txt','r') as f:
            for line in f:
                line = line.strip("\n")
                (key, val) = line.split("-")
                mypasses[str(key)] = val

        return mypasses

    def changesettings(self):
        print("Current security is level %s." %self.security)

        while True:
            s = raw_input("New security level: ")
            if s.isdigit(): self.security = int(s); self.setsettings(); break
            else: print("Must enter number between 1 and 4.")

        print("Settings saved.\n")

    def exe(self, choice):
        print("")
        if choice == "1": self.savepass()
        elif choice == "2": self.getpass()
        elif choice == "3": self.changesettings()
        elif choice == "4": quit()


class User():
    def register(self):
        self.user = raw_input("Enter new username: ")
        self.passw = pass_input("Enter new password: ")
        self.saveuser(); self.run()

    def login(self):
        self.getuser()

        u = raw_input("Enter your username: ")
        p = pass_input("Enter your password: ")

        if u == self.user and p == self.passw:
            self.run()
        else:
            print("INCORRECT PASSWORD.")

    def saveuser(self):
        with open('myacc.txt','w') as file:
            file.write(self.user + "-" + self.passw)
        with open('mypass.txt','w') as file:
            file.write("")

    def getuser(self):
        with open('myacc.txt','r') as f:
            self.user, self.passw = f.read().split('-')

    def run(self):
        pass_gen = PasswordGenerator(security=4)
        print("--*-- PASSWORD GENERATOR --*--")
        while True:
            print("--*-- 1. Make Password")
            print("--*-- 2. Get Password")
            print("--*-- 3. Settings")
            print("--*-- 4. Quit")
            pass_gen.exe(raw_input("--*-- > "))


def main():
    user = User()
    if isfile(getcwd()+'/myacc.txt'):
        user.login()
    else:
        user.register()

if __name__ == '__main__':
    main()

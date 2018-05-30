# PASSWORD GENERATOR BY WILL ASSAD

# IMPORTS
import random
import time
import getpass
from time import sleep
import hashlib


# FUNCTIONS
def savePasswords(typePassword, password):
    fileName = "mypasswords.txt"
    file = open(fileName, 'a')
    text = typePassword + ": " + password
    file.write("%s\n" % text)
    file.close()


def passwordGenerator():
    characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                  "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
                  "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8",
                  "9", "0", "!"]

    numCharacters = random.randint(8, 20)

    passwordList = []

    for x in range(0, numCharacters):
        passwordList.append(random.choice(characters))

    password = ''.join(str(n) for n in passwordList)

    typePassword = input("\nWhat site would you like to make a password for? (e.g. instagram)  ")
    print("%s is your new password for %s." % (password, typePassword))
    sleep(3)
    print("\nThe password has been saved to \"mypasswords.txt\".")
    savePasswords(typePassword, password)


# MAIN

runAgain = True

file = open("user.txt", "r")
first = file.read(1)
second = file.read(2)
if not first or not second:
    username = ""

for enteredValue in file:
    enteredValue = enteredValue.strip()
    enteredValue = enteredValue.strip("\n")
    enteredValue = enteredValue.strip("'")
    username = enteredValue

if username == "":
    print("\nWelcome to the Password Generator!")
    sleep(2)
    newUser = input("Create your new username: ")
    fileName = "user.txt"
    file = open(fileName, 'a')
    username = newUser
    file.write("%s\n" % username)
    file.close()
    sleep(1)

file = open("privatekey.txt", "r")

first = file.read(1)
second = file.read(2)
if not first or not second:
    key = ""

for enteredValue in file:
    enteredValue = enteredValue.strip()
    enteredValue = enteredValue.strip("\n")
    enteredValue = enteredValue.strip("'")
    key = enteredValue

if key == "":
    newPass = input("Create your new password: ")
    fileName = "privatekey.txt"
    file = open(fileName, 'a')
    hashedGuess = hashlib.sha256(newPass.encode('utf-8')).hexdigest()
    file.write("%s\n" % hashedGuess)
    file.close()
    sleep(1)

enteredUser = input("\nEnter username: ")
file1 = open("user.txt", "r")
for enteredValue in file1:
    enteredValue = enteredValue.strip()
    enteredValue = enteredValue.strip("\n")
    enteredValue = enteredValue.strip("'")
    username = enteredValue

if enteredUser == username:
    file2 = open("privatekey.txt", "r")
    for enteredValue in file2:
        enteredValue = enteredValue.strip()
        enteredValue = enteredValue.strip("\n")
        enteredValue = enteredValue.strip("'")
        privateKey = enteredValue

    enteredPass = getpass.getpass("\nEnter the private key: ")
    hashedGuess = hashlib.sha256(enteredPass.encode('utf-8')).hexdigest()

    while runAgain == True:
        if hashedGuess == privateKey:
            again = True
            while again == True:
                print("\n1. Generate a New Password")
                print("2. View an Old Password")
                print("3. Enter pre-existing password")
                choice = input("\nWhich one (1,2,3): ")

                if choice == "1":
                    passwordGenerator()
                    sleep(2)
                    anotherOne = input("\nPress q to quit or any key to perform another task.")
                    if anotherOne == "q":
                        runAgain = False
                    else:
                        runAgain = True
                    break

                elif choice == "2":
                    whichOne = input("What site was your password from? (e.g. facebook)  ")
                    myPasswords = []

                    file = open("mypasswords.txt", "r")

                    for enteredValue in file:
                        enteredValue = enteredValue.strip()
                        enteredValue = enteredValue.strip("\n")
                        enteredValue = enteredValue.strip("'")
                        myPasswords.append(enteredValue)

                        if whichOne in enteredValue:
                            print("\n%s" % (enteredValue))
                            value = True
                            break
                        else:
                            value = False

                    if value == False:
                        print("\nSorry, couldn't find that password.")
                        print("Here are all your saved passwords:")
                        print("\n")

                        for x in range(0, 3):
                            del myPasswords[0]

                        length = len(myPasswords)

                        sleep(3)
                        for x in range(0, length):
                            print(myPasswords[x])

                    sleep(2)
                    anotherOne = input("\nPress q to quit or any key to perform another task.")
                    if anotherOne == "q":
                        runAgain = False
                    else:
                        runAgain = True
                    break


                elif choice == "3":
                    typePassword = input("\nWhat site would you like to make a password for? (e.g. instagram)  ")
                    password = input("Enter the password: ")
                    sleep(2)
                    print("\nThe password has been saved to \"mypasswords.txt\".")
                    savePasswords(typePassword, password)

                    sleep(2)
                    anotherOne = input("\nPress q to quit or any key to perform another task.")
                    if anotherOne == "q":
                        runAgain = False
                    else:
                        runAgain = True
                    break
                else:
                    print("Sorry, I didn't understand that command.")
                    sleep(2)
                    print("Try again by entering a 1 or a 2.")
                    sleep(2)
        else:
            print("\nIncorrect Password.")
            break
else:
    print("That is the wrong username.")
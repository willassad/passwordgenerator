#PASSWORD GENERATOR BY WILL ASSAD

#IMPORTS
import random
import time
from time import sleep

#FUNCTIONS
def savePasswords(typePassword,password):
    fileName = "mypasswords.txt"
    file = open(fileName, 'a')
    text= typePassword+": "+password
    file.write("%s\n" %text)
    file.close()


def passwordGenerator():
    
    characters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0","!"]
    
    numCharacters=random.randint(8,20)
    
    passwordList=[]
    
    for x in range(0,numCharacters):
        passwordList.append(random.choice(characters))

    password = ''.join(str(n) for n in passwordList)
    
    typePassword=raw_input("\nWhat site would you like to make a password for? (e.g. instagram)  ")
    print "%s is your new password for %s." %(password,typePassword)
    sleep(3)
    print "\nThe password has been saved to \"mypasswords.txt\"."
    savePasswords(typePassword,password)



#MAIN
again=True
while again==True:
    print "\n1. Generate a New Password"
    print "2. View an Old Password"
    choice= raw_input("\nWhich one (1 or 2): ")
    
    if choice=="1":
        passwordGenerator()
        break
    
    elif choice=="2":
        whichOne=raw_input("What site was your password from? (e.g. facebook)  ")
        myPasswords=[]
        
        file = open("mypasswords.txt", "r") 
        for enteredValue in file: 
            enteredValue = enteredValue.strip()
            enteredValue = enteredValue.strip("\n")
            enteredValue = enteredValue.strip("'")
            myPasswords.append(enteredValue)
            
            if whichOne in enteredValue:
                print "\n%s" %(enteredValue)
                value = True
                break
            else:
                value = False
        
                   
        if value==False:
            print "\nSorry, couldn't find that password."
            print "Here are all your saved passwords:"
            print "\n"
        
            del myPasswords[0]
            del myPasswords[0]
            del myPasswords[0]
            length=len(myPasswords)
        
            for x in range(0,length):
                print myPasswords[x]               
        break
  
    
    else:  
        print "Sorry, I didn't understand that command."
        sleep(2)
        print "Try again by entering a 1 or a 2."
        sleep(2)  
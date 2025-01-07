import os
import random
import time
def q1():
    print("What is 1 + 1?:")
    x = input("a: 3\nb: 2\nc: 7\nd: 825976\n")
    if x.lower() == "b":
        print("Correct")
    else:
        print("Incorrect")
def q2():
    print("What is the code for a 500kg bomb in Helldivers 2?")
    x = input("a: wsdwa\nb: wdsd\nc: wdsss\nd: swaswdsw\n")
    if x.lower() == "c":
        print("Correct")
    else:
        print("Incorrect")

def q3():
    print("When was the second batlle of malevelon creek?")
    x = input("a: April 7th\nb: may 3rd\nc: april 3rd\nd: april 1st\n")
    if x.lower() == "d":
        print("Correct")
    else:
        print("Incorrect")
def q4():
    print("What movie was Helldivers based off of?")
    x = input("a:Star wars\nb:Star trek\nc:Starship Troopers\nd:SpongeBob Sponge on the Run\n")
    if x.lower() == "c":
        print("Correct")
    else:
        print("Incorrect")


functions = [q1, q2, q3, q4]
random.shuffle(functions)
for func in functions:
    func()
    time.sleep(1.5)
    os.system('cls')


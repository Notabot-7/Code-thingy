#Auto Clicker V1.0
#By: Jack W, special credit to Jack C

'''
This program will automatically left-click the mouse when F7 is pressed, to turn off press F7 again.
I recommend putting 0.00001 just to be sure you reach the limit of 10 cps. Very sorry it can't click faster.
The program will close down and crash when the mouse gets too close to the corner of the screen, this is a failsafe of VS code that I will not be removing as it is not recommended.
'''

import keyboard
import pyautogui
import time

def autoclicker(interval):
    print("Move your mouse to the desired position. Autoclicker will start when F7 is pressed. ")
    click_on = True
    program_on = True

    while program_on:
        keyboard.wait('F7')
        print('on')
        click_on = True
        while click_on == True:
            pyautogui.click()
            time.sleep(interval)
            if keyboard.is_pressed('F7'):
                print('off')
                click_on = False
        

if __name__ == "__main__":

    while True:
        try:
            click_interval = float(input("Enter the time interval clicks (in seconds): "))

            if click_interval < 0:
                raise ValueError("Number must be positive. Please try again")
            break
        except ValueError as e:
            print('Please enter a number')
    
    


    
    autoclicker(click_interval)
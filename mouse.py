import pyautogui
import numpy as np
import math


def auto_mice():
    y=input('Hello Kindly Enter Duration In SECONDS For Which You Want To Run The Program: ')
    try: 
        x=int(y)
        np.random.seed(42)
        a=np.random.randint(0,x, size=(x,1))
        print(f'Auto Mice will now work for next {x} seconds; Kindly press ctr + alt + del to stop')
        for i in a:
            
            pyautogui.moveTo(i,200,duration=1)
    except ValueError:
        print('Wrong Input. Kindly Enter in Digits Only')
    

auto_mice()
#############################################################################
#  Module name               : Bell.py                                      #
#  Standard Imports          : time, os, datetime,winsound                  #
#  Function(schoolBell(h,m)) : Plays bell as per given instructions         #
#  Coded By                  : Ms. Sana Sampson                             #
#############################################################################

# ---- time : system time
#sleep(seconds) : Delays execution for a given number of seconds. 
import time

# ---- time : datetime
#Programs that import and use 'os' stand a better chance of being
#portable between different platforms. 
import os

#datetime.now() : Returns current date and time
from datetime import datetime 

# ---- winsound
#PlaySound(sound, flags) - play a sound
#SND_FILENAME - sound is a wav file name
import winsound

def schoolBell(Hour,Minute):
    '''
Takes input as (Hour,Minute) in 24 hour format and plays a bell sound file as per system time
    '''
    userHour = Hour
    userMin = Minute
    
    Played = False
    #print('\nThe bell will be played as per the requested time!')
    while True:
        now = datetime.now()
        currentHour = now.hour
        currentMin = now.minute
        
        if currentHour == userHour and currentMin == userMin and not Played:
            Played = True
            winsound.PlaySound('Bell.wav', winsound.SND_FILENAME)
            break
       


# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 08:26:36 2020

@author: Adit Sharma
"""

import winsound
from win10toast import ToastNotifier

def timer (remider,seconds):
    notificator=ToastNotifier()
    notificator.show_toast("Reminder",f"""Alarm will go off in {seconds} Seconds.""",duration=20)
    notificator.show_toast(f"Reminder",remider,duration=20)

    #alarm
    frequency=2500
    duration=1000
    winsound.Beep(frequency,duration)

if __name__=="__main__":
    words=input("What would you remindes of: ")
    sec=int(input("Enter seconds: "))
    timer(words,sec)

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 08:11:11 2020

@author: (GD) ShadowPlague
"""
import win32gui, win32com.client
import time

def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

def find_program():
    programs = []
    win32gui.EnumWindows(windowEnumerationHandler, programs) # Enumerates all running programs
    return(programs)

def execc(name, listt):
    for i in listt:
        if name in i[1]:
            doom = win32com.client.Dispatch("WScript.Shell")
            doom.SendKeys('%')
            win32gui.SetForegroundWindow(i[0])
            win32gui.MoveWindow(i[0], 1562, 631, 427, 408, True)
            break

for each in find_program():
    print(each)
process = input('Choose a program from the list above (Name Only): ')

target = input('Wanted time of operation? ')
constant = time.perf_counter()

print('Note: not all programs can be handled this way\n')
time.sleep(2)

t = 0
try:
    print('Success!')
    while t<float(target):
        execc(str(process),find_program())
        
        t = time.perf_counter()-constant
        print('Operation time is:',round(t,1))
        
        time.sleep(.1)
except:
    print('Not found')
  

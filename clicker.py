import pyautogui as py
import tkinter as tk
import time

currentsetting = "Cursor"

settingslist = [
    "Location",
    "Cursor",
]

def changeclicksettings(event):
    global currentsetting
    for setting in settingslist:
        if setting == currentsetting:
            s1 = settingslist.index(setting)
            s2 = (s1 + 1) % len(settingslist)
            currentsetting = settingslist[s2]
            updateclicksettings()
            break

def updateclicksettings():
    global currentsetting
    settings.config(text="Click on: " + currentsetting)
    print('changed click settings to ' + currentsetting)

def clickcursor():
    x, y = py.position()
    py.click(x, y)
    print('clicked at ' +str(x) + ', ' + str(y))

def handleclick(event):
    global currentsetting
    if currentsetting == "Cursor":
        togglecountdown()
        root.after(3000, clickcursor)
    else:
        #change this, temp.
        changeclicksettings(0)

def togglecountdown():
    global countdownstatus
    if "countdown: disabled" in countdownstatus.cget('text'):
        for i in range(3, -1, -1):
            root.after((3-i)*1000, lambda i=i: (print('clickcountdown: '+str(i)), countdownstatus.config(text='countdown: active ('+str(i)+')')))
        root.after(4000, lambda: countdownstatus.config(text='countdown: disabled (0)'))
    else:
        print('countdown is already counting')

root = tk.Tk()

root.title("Best Auto Clicker")
root.geometry("500x500")

title = tk.Label(root, text="Best Auto Clicker", font=("Arial", 20))
title.pack()

madeinus = tk.Label(root, text="Made in the USA", font=("Arial", 10))
madeinus.pack()

settings = tk.Button(root, text="")
settings.bind("<Button-1>", changeclicksettings)
settings.pack()
changeclicksettings(0)

clickbutton = tk.Button(root, text="CLICK")
clickbutton.bind("<Button-1>", handleclick)
clickbutton.pack()

countdownstatus = tk.Label(root, text="countdown: disabled (0)", font=("Arial", 10))
countdownstatus.pack()

root.mainloop()

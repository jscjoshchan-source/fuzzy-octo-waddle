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
    settings.config(text="Enable Click on " + currentsetting)
    print('changed click settings to ' + currentsetting)

def clickcursor():
    x, y = py.position()
    py.click(x, y)
    print('clicked at ' +str(x) + ', ' + str(y))

def handleclick(event):
    global currentsetting
    if currentsetting == "Cursor":
        togglecountdown()
        #root.after(3000, clickcursor)
    else:
        #change this, temp.
        changeclicksettings(0)

def togglecountdown():
    global countdownstatus
    if "countdown: paused" in countdownstatus.cget('text'):
        countdownstatus.config(text="countdown: running (3)")
        for i in range(0, 3, 1):
            STRi = str(i)
            print('init'+STRi)
            root.after(1000 * i, lambda: print('stalling'+STRi))
            print('ainit'+STRi)

def test():
    for i in range(5):
        root.after(1000*i, lambda: print('stalling'+str(i)))

root = tk.Tk()

root.title("Best Auto Clicker")
root.geometry("500x500")

title = tk.Label(root, text="Best Auto Clicker", font=("Arial", 20))
title.pack()

madeinus = tk.Label(root, text="Made in the USA", font=("Arial", 10))
madeinus.pack()

countdownstatus = tk.Label(root, text="countdown: paused (0)", font=("Arial", 5))
countdownstatus.pack()

settings = tk.Button(root, text="")
settings.bind("<Button-1>", changeclicksettings)
settings.pack()
changeclicksettings(0)

clickbutton = tk.Button(root, text="CLICK")
clickbutton.bind("<Button-1>", handleclick)
clickbutton.pack()

root.mainloop()

test()
root.quit()
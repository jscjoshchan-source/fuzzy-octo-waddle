### IMPORT AREA -start
import tkinter as tk
import pyautogui as py
import time
###IMPORT AREA -end
###FUNCTIONS AREA -start
def click(event):
    print('clicked smth')
def exit(event):
    root.quit()
    py.click(1085, 950)
    print("quit best auto clicker and entered VS CODE")
### FUNCTIONS AREA -end
### CREATING WINDOWS AREA -start
root = tk.Tk()
root.title("Best Auto Clicker")
root.geometry("500x500")
### CREATING WINDOWS AREA -end
### CREATING LABELS/BUTTONS/OTHER AREA -start

title = tk.Label(root, text="Welcome to Best Auto Clicker", font=("Arial", 20))
title.pack()

subtext = tk.Label(root, text="Made in the USA", font=("Arial", 10))
subtext.pack()

click_button = tk.Button(root, text="Click")
click_button.pack()
### CREATING LABELS/BUTTONS/OTHER AREA -end
### KEYBINDS AREA -start
click_button.bind("<Button-1>", click)

root.bind("q", exit)
root.bind("g", lambda event: py.click(250, 950))
root.bind("f", lambda event: py.click(95, 950))
### KEYBINDS AREA -end
### MAINLOOP AREA -start
root.mainloop()
### MAINLOOP AREA -end
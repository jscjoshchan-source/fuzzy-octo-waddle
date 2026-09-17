import tkinter as tk
import pyautogui as py
import time

root = tk.Tk()
#root2 = tk.Tk()

#create main window
root.title("Auto Clicker")
root.geometry("300x300")

#create text label
label = tk.Label(root, text="Auto Clicker", font=("Arial", 12))

#make it visible
label.pack(pady=5)

#start loop to keep window open
root.mainloop()

#click
py.countdown(10)
py.click(1000, 1000)
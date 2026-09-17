import tkinter as tk

root = tk.Tk()
root.title("Best Auto Clicker")
root.geometry("500x500")

title_welcome = tk.Label(root, text="Welcome to Best Auto Clicker", font=("Arial", 20))
title_welcome.pack()

created_by = tk.Label(root, text="Made in the USA", font=("Arial", 10))
created_by.pack()

root.mainloop()
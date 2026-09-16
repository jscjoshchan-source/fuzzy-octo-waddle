import tkinter as tk
root = tk.Tk()

#create main window
root.title("Auto Clicker")
root.geometry("300x300")

#create text label
label = tk.Label(root, text="Auto Clicker", font=("Arial", 12))

#make it visible
label.pack(pady=5)

#start loop to keep window open
root.mainloop()
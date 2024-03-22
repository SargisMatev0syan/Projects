# By creating a digital clock in Python using the 'datetime' module to get
#  the current time and the 'tkinter' library to create a graphical
#  user interface (GUI)  for the clock display.

import tkinter as tk
from datetime import datetime

def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)  # Update time every 1000 milliseconds (1 second)

#Creating the main window
root = tk.Tk()
root.title('Digital Clock')
root.geometry('200x100')    

# Creating a label to display the clock
clock_label = tk.Label(root, font=("Arial", 30), bg="black", fg="white")
clock_label.pack(fill=tk.BOTH, expand=1)

#Start updating time
update_time()

root.mainloop()
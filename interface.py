import tkinter as tk
from tkinter import ttk

tasks = ['Task A', 'Task B', "Task C"]

# window
window = tk.Tk()
window.title('demo')
window.geometry('300x150') #('HeightxWidth')

# title
title_label = ttk.Label(master = window, text = 'Daily Tasks',font = 'Calibri 24 bold') #('Font Size Extra')
title_label.grid(row = 0, column = 0, pady = 2)

# initial tasks
def packing():
    for i in range(0,len(tasks)):
        checkbox = ttk.Checkbutton(master = window, text = tasks[i])
        checkbox.grid(row = 4 + i, column = 0, pady = 2)
packing()

# add task
def addTask():
    if len(entry_str.get()) > 0:
        tasks.append(entry_str.get())
        packing()

# input field
input_frame = ttk.Frame(master = window)
entry_str = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_str)
button = ttk.Button(master = input_frame, text = 'Add Task', command = addTask )
entry.grid(row = 1, column = 0, pady = 2) 
button.grid(row = 2, column = 0, pady = 2)
input_frame.grid(row = 3, column = 0, pady = 2)


# run
window.mainloop()
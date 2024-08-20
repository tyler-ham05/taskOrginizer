import tkinter as tk
from tkinter import ttk

tasks = ['Task A', 'Task B', "Task C"]

# window
window = tk.Tk()
window.title('demo')
window.geometry('300x150') #('HeightxWidth')

# title
title_label = ttk.Label(master = window, text = 'Daily Tasks',font = 'Calibri 24 bold') #('Font Size Extra')
title_label.pack()

# input field
"""for i in range(0,len(tasks)):
    checkbox = ttk.Checkbutton(master = window, text = tasks[0]).grid(row=i)
    checkbox.pack()"""
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = 'Add Task')
entry.pack(side = 'bottom') 
button.pack(side = 'bottom')
input_frame.pack(pady = 10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack()

# run
window.mainloop()
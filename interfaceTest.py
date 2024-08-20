import tkinter as tk
from tkinter import ttk

def convert():
    print(entry.get()) #inefficient, better to store var in variable as seen in entry_int in the input field
    #output_string.set('test')
    output_string.set(entry_int.get() * 1.61)

# window
window = tk.Tk()
window.title('demo')
window.geometry('300x150') #('HeightxWidth')

# title
title_label = ttk.Label(master = window, text = 'Miles to Kilometers',font = 'Calibri 24 bold') #('Font Size Extra')
title_label.pack()

# input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = 'Convert', command = convert)
entry.pack(side = 'left', padx = 10) 
button.pack(side = 'right')
input_frame.pack(pady = 10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack()

# run
window.mainloop()
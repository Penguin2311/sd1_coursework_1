from tkinter import *
from tkinter import ttk

from pip import main

root = Tk()
root.title('Salary Calculator')

mainframe = ttk.Frame(root, padding="5 5 5 5")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Speed:").grid(column=1, row=1, sticky=W)
speed = IntVar()
speed_entry = ttk.Entry(mainframe, width=3, textvariable=speed)
speed_entry.grid(column=2, row=1)


ttk.Label(mainframe, text="Shooting:").grid(column=1, row=2, sticky=W)
shooting = IntVar()
shooting_entry = ttk.Entry(mainframe, width=3, textvariable=shooting)
shooting_entry.grid(column=2, row=2)

ttk.Label(mainframe, text="Passing:").grid(column=1, row=3, sticky=W)
passing = IntVar()
passing_entry = ttk.Entry(mainframe, width=3, textvariable=passing)
passing_entry.grid(column=2, row=3)

ttk.Label(mainframe, text=".").grid(column=3, row=1, padx=100, pady=100)

ttk.Label(mainframe, text="Defending:").grid(column=4, row=1, sticky=W)
defending = IntVar()
defending_entry = ttk.Entry(mainframe, width=3, textvariable=defending)
defending_entry.grid(column=5, row=1)

ttk.Label(mainframe, text="Dribbling:").grid(column=4, row=2, sticky=W)
dribbling = IntVar()
dribbling_entry = ttk.Entry(mainframe, width=3, textvariable=dribbling)
dribbling_entry.grid(column=5, row=2)

ttk.Label(mainframe, text="Physicality:").grid(column=4, row=3, sticky=W)
physicality = IntVar()
physicality_entry = ttk.Entry(mainframe, width=3, textvariable=physicality)
physicality_entry.grid(column=5, row=3)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()

print(speed)
from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = speed.get()+shooting.get()+passing.get()+dribbling.get()+defending.get()+physicality.get()
        overall_rate.set(value*100/30)
        ttk.Label(mainframe, text="Overall rate is ").grid(column=0, row=5)
        ttk.Label(mainframe, textvariable=overall_rate).grid(column=1, row=5)

        salary.set(1000)
        ttk.Label(mainframe, text="Salary is ").grid(column=0, row=7)
        ttk.Label(mainframe, textvariable=salary).grid(column=1, row=7)

    except ValueError:
        pass


root = Tk()
root.title('Salary Calculator')

mainframe = ttk.Frame(root, padding="5 5 5 5")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


input_frame = ttk.Frame(mainframe, padding="10 5 10 5")
input_frame.grid(column=0, row=0)

ttk.Label(input_frame, text="Speed: ", font=("Proxima nova", 13)).grid(column=1, row=1, sticky=W)
speed = IntVar()
speed_entry = ttk.Entry(input_frame, width=2, textvariable=speed)
speed_entry.grid(column=2, row=1)

ttk.Label(input_frame, text="Shooting: ", font=("Proxima nova", 13)).grid(column=1, row=2, sticky=W)
shooting = IntVar()
shooting_entry = ttk.Entry(input_frame, width=2, textvariable=shooting)
shooting_entry.grid(column=2, row=2)

ttk.Label(input_frame, text="Passing: ", font=("Proxima nova", 13)).grid(column=1, row=3, sticky=W)
passing = IntVar()
passing_entry = ttk.Entry(input_frame, width=2, textvariable=passing)
passing_entry.grid(column=2, row=3)

ttk.Label(input_frame, text="").grid(column=3, row=1, padx=20)

ttk.Label(input_frame, text="Defending: ", font=("Proxima nova", 13)).grid(column=4, row=1, sticky=W)
defending = IntVar()
defending_entry = ttk.Entry(input_frame, width=2, textvariable=defending)
defending_entry.grid(column=5, row=1)

ttk.Label(input_frame, text="Dribbling: ", font=("Proxima nova", 13)).grid(column=4, row=2, sticky=W)
dribbling = IntVar()
dribbling_entry = ttk.Entry(input_frame, width=2, textvariable=dribbling)
dribbling_entry.grid(column=5, row=2)

ttk.Label(input_frame, text="Physicality: ", font=("Proxima nova", 13)).grid(column=4, row=3, sticky=W)
physicality = IntVar()
physicality_entry = ttk.Entry(input_frame, width=2, textvariable=physicality)
physicality_entry.grid(column=5, row=3)


input_error_frame = ttk.Frame(mainframe, padding = "10 5 5 5")
input_error_frame.grid(column=0, row=1)



overall_rate = StringVar()
salary = IntVar()

ttk.Button(mainframe, text="Calculate Salary", command=calculate).grid(column=0, row=4, sticky=W)

root.mainloop()
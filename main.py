'''
https://tkdocs.com/ documentation was used for the majority of this project
'''

from tkinter import *
from tkinter import ttk
import sv_ttk


def salary_calculation(overall: float) ->str:
    '''
    Takes overall rate as an argument. The salary table is stored as a dictionary with salary:overall item pairs.
    Loops over each item and gives salary an upper and lower bound accordingly. Returns it as a string.
    '''

    salary_table = { 1000: 80,
                     700: 60,
                     500: 45,
                     400: 30}
    
    salary_upper = ""
    salary_lower = ""
    for key, value in salary_table.items():
        if overall > value:
            salary_lower = key
            break
        elif overall == value:
            salary_upper = ""
            salary_lower = key
            break
        else:
            salary_upper = key

    salary = "{} {}".format(salary_upper, salary_lower)
    return salary.strip()


def calculate():
    '''
    gets the value of all 6 variable to calculates overall rate, passes it to the salary_calculation function to get salary.
    Creates required labels to display both.
    '''
    value = speed.get()+shooting.get()+passing.get()+dribbling.get()+defending.get()+physicality.get()
    overall_rate.set(round(value*100/30, 2))

    ttk.Label(overall_frame, text="Overall rate is ", font=("Proxima nova", 11)).grid(column=0, row=0)
    ttk.Label(overall_frame, textvariable=overall_rate, font=("Proxima nova", 11)).grid(column=1, row=0)

    salary.set(salary_calculation(overall_rate.get()))
    ttk.Label(salary_frame, text="Salary is ", font=("Proxima nova", 11)).grid(column=0, row=0)
    ttk.Label(salary_frame, textvariable=salary, font=("Proxima nova", 11)).grid(column=1, row=0)


#main window
root = Tk()
root.title('Salary Calculator')


#mainframe
mainframe = ttk.Frame(root, padding="5 5 5 5")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))


#contains all 6 attributes needed to be input
input_frame = ttk.Frame(mainframe)
input_frame.grid(column=0, row=0, sticky=W)


speed_frame = ttk.Frame(input_frame)
speed_frame.grid(column=0, row=0, sticky=W)
ttk.Label(speed_frame, text="Speed:", font=("Proxima nova", 11)).grid(column=0, row=0, sticky=W)
speed = IntVar()
ttk.Label(speed_frame, textvariable=speed, font=("Proxima nova", 11)).grid(column=1, row=0, sticky=W)


#https://stackoverflow.com/a/38168041 ttk scale gives a decimal number as a string as its output, the command given to the scale converts it to int.
speed_entry = ttk.Scale(speed_frame, length = 100, orient=HORIZONTAL, from_=0, to=5, command = lambda s: speed.set(int(float(s))))
speed_entry.grid(column=0, row=1, columnspan=2, sticky=W, pady=5)


shooting_frame = ttk.Frame(input_frame)
shooting_frame.grid(column=0, row=1, sticky=W)
ttk.Label(shooting_frame, text="Shooting:", font=("Proxima nova", 11)).grid(column=0, row=0, sticky=W)
shooting = IntVar()
ttk.Label(shooting_frame, textvariable=shooting, font=("Proxima nova", 11)).grid(column=1, row=0, sticky=W)
shooting_entry = ttk.Scale(shooting_frame, length = 100, orient=HORIZONTAL, from_=0, to=5, command = lambda s: shooting.set(int(float(s))))
shooting_entry.grid(column=0, row=1, columnspan=2, sticky=W, pady=5)


passing_frame = ttk.Frame(input_frame)
passing_frame.grid(column=0, row=2, sticky=W)
ttk.Label(passing_frame, text="Passing:", font=("Proxima nova", 11)).grid(column=0, row=0, sticky=W)
passing = IntVar()
ttk.Label(passing_frame, textvariable=passing, font=("Proxima nova", 11)).grid(column=1, row=0, sticky=W)
passing_entry = ttk.Scale(passing_frame, length = 100, orient=HORIZONTAL, from_=0, to=5, command = lambda s: passing.set(int(float(s))))
passing_entry.grid(column=0, row=1, columnspan=2, sticky=W, pady=5)


defending_frame = ttk.Frame(input_frame)
defending_frame.grid(column=1, row=0, sticky=W)
ttk.Label(defending_frame, text="Defending:", font=("Proxima nova", 11)).grid(column=0, row=0, sticky=W)
defending = IntVar()
ttk.Label(defending_frame, textvariable=defending, font=("Proxima nova", 11)).grid(column=1, row=0, sticky=W)
defending_entry = ttk.Scale(defending_frame, length = 100, orient=HORIZONTAL, from_=0, to=5, command = lambda s: defending.set(int(float(s))))
defending_entry.grid(column=0, row=1, columnspan=2, sticky=W, pady=5)


dribbling_frame = ttk.Frame(input_frame)
dribbling_frame.grid(column=1, row=1, sticky=W)
ttk.Label(dribbling_frame, text="Dribbling:", font=("Proxima nova", 11)).grid(column=0, row=0, sticky=W)
dribbling = IntVar()
ttk.Label(dribbling_frame, textvariable=dribbling, font=("Proxima nova", 11)).grid(column=1, row=0, sticky=W)
dribbling_entry = ttk.Scale(dribbling_frame, length = 100, orient=HORIZONTAL, from_=0, to=5, command = lambda s: dribbling.set(int(float(s))))
dribbling_entry.grid(column=0, row=1, columnspan=2, sticky=W, pady=5)


physicality_frame = ttk.Frame(input_frame)
physicality_frame.grid(column=1, row=2, sticky=W)
ttk.Label(physicality_frame, text="Physicality:", font=("Proxima nova", 11)).grid(column=0, row=0, sticky=W)
physicality = IntVar()
ttk.Label(physicality_frame, textvariable=physicality, font=("Proxima nova", 11)).grid(column=1, row=0, sticky=W)
physicality_entry = ttk.Scale(physicality_frame, length = 100, orient=HORIZONTAL, from_=0, to=5, command = lambda s: physicality.set(int(float(s))))
physicality_entry.grid(column=0, row=1, columnspan=2, sticky=W, pady=5)


#adds padding to all children of input_frame
for child in input_frame.winfo_children(): 
    child.grid_configure(padx=15, pady=5)



overall_rate = IntVar()
salary = StringVar()

#Button to call the calculate function
ttk.Button(mainframe, text="Calculate Salary", command=calculate).grid(column=0, row=2, pady= 10)


output_frame = ttk.Frame(mainframe)
output_frame.grid(column=0, row=3, sticky=W)

overall_frame = ttk.Frame(output_frame)
overall_frame.grid(column=0, row=0, sticky=W, padx=5)

salary_frame = ttk.Frame(output_frame)
salary_frame.grid(column=0, row=1, sticky=W, padx=5)

#applying the installed theme
sv_ttk.set_theme("dark")


root.mainloop()
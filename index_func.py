from tkinter import *

counter = 0
def action_butt():
    global counter
    counter += 1
    count.config(text="Number of uses : {}".format(counter))


# Create Tk instance
window = Tk()


# set size tab
"""
window.minsize(400,300)
window.maxsize(600,500)
"""


window.geometry("600x500")
window.resizable(width=False, height=False)


# The name of the program page
window.title('Calculate BMI')


# Title of the program
Label(window, text="Calculate body BMI",
      font=("arial", 14),
      fg="blue", bg="white").pack()


# counter
count = Label(window, font=("arial", 14), fg="white", bg="blue")
count.config(text="Number of uses : 0")
count.pack()


# Definition of Gender
gender = Label(window, text="Male / Female")
gender.config(fg="red")
gender.pack()


# Calculate button
cal_butt = Button(window, text="Enter")
cal_butt.config(bg="yellow", fg="black")
cal_butt.config(command=action_butt)
cal_butt.pack()


# Developer name
Label(window, text="Developed by Sadegh", 
      font=("Tahoma", 12), 
      foreground="white", background="blue" ).pack()


# Create run loop
window.mainloop()
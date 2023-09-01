from tkinter import *

counter = 0
def action_butt():
      global counter
      counter += 1
      count.config(text="Number of uses : {}".format(counter))
      result.config(text="result is : {}/{}".format(height.get(), weight.get()))
      
      if is_free.get() == 1 :
            free_status.config(text="Use Free, enjoy!")
      else :
            free_status.config(text=".")



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



# Counter
count = Label(window, font=("arial", 14), fg="white", bg="blue")
count.config(text="Number of uses : 0")
count.pack()




# Entry height / Weight

Label(window, text="Enter height").pack()
height = Entry(window)
height.pack()

Label(window, text="Enter weight").pack()
weight = Entry(window)
weight.pack()



# result

result = Label(window, text="....")
result.config(fg="red")
result.pack()


# Calculate button

cal_butt = Button(window, text="Enter")
cal_butt.config(bg="yellow", fg="black")
cal_butt.config(command=action_butt)
cal_butt.pack()



# Check Free Use
is_free = IntVar()
Checkbutton(window, text="Free", variable=is_free).pack()

free_status = Label(window, text=".")
free_status.config(fg="green")
free_status.pack()


# Create run loop
window.mainloop()
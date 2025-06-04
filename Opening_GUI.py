from tkinter import *

mngr = Tk()
mngr.geometry('520x540')
mngr.title("Password Manager")

gui_header = Label(mngr)
gui_header.place(x=60,y=50)

def nextPage():
    mngr.destroy()
    import Input_Information

def prevPage():
    mngr.destroy()
    import Random_Password_Generator

def otherPage():
    mngr.destroy()
    import Search_Passwords

int_inf = Button(mngr, text="Input Information", command=nextPage, bg='antiquewhite4',fg='white', font=("times",16,"bold")).pack(fill=BOTH, expand=TRUE, side=TOP)
Rand_pass_gen = Button(mngr, text="Random Password Generator", command=prevPage, bg='antiquewhite3',fg='white', font=("times",16,"bold")).pack(fill=BOTH, expand=TRUE, side=TOP)
Ser_func = Button(mngr, text="Search Passwords", command=otherPage, bg='bisque3',fg='white', font=("times",16,"bold")).pack(fill=BOTH, expand=TRUE, side=BOTTOM)

mngr.mainloop()
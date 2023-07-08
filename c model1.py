from tkinter import *
from tkinter.font import Font
root = Tk()
root.title("calculator")

input = Entry(root,justify="right",width=13,font=("Digital-7",50),bg="chartreuse2",fg="Black",selectbackground="chartreuse4")
input.grid(row=0,column=0,columnspan=4,padx=60,pady=15)
def click(num):
    crnt= input.get()
    input.delete(0,END)
    input.insert(0,str(crnt) + str(num))
    return

def add():
    crnt=input.get()
    global fnum
    global operation
    operation="add"
    fnum= int(crnt)
    input.delete(0,END)
    return

def sub():
    crnt=input.get()
    global fnum
    global operation
    operation="sub"
    fnum= int(crnt)
    input.delete(0,END)
    return

def mult():
    crnt=input.get()
    global fnum
    global operation
    fnum= int(crnt)
    operation="mult"
    input.delete(0,END)
    return

def div():
    crnt=input.get()
    global fnum
    fnum= int(crnt)
    global operation
    operation="div"
    input.delete(0,END)
    return

def clear():
    input.delete(0,END)
    return

def equal():
    crnt=input.get()
    snum=int(crnt)
    input.delete(0,END)
    if operation=="add":
        input.insert(0,str(fnum+snum))
    elif operation=="sub":
        input.insert(0,str(fnum-snum))
    elif operation=="mult":
        input.insert(0,str(fnum*snum))
    elif operation=="div":
        input.insert(0,str(fnum/snum))
    
    returnfg=""


button_1 = Button(root,text="1",padx=64,font=("Bold",15),pady=25,fg="Black",bg="#c7ecee",activebackground="#636e72",command=lambda: click(1))
button_2 = Button(root,text="2",padx=58,font=("Bold",15),pady=25,fg="Black",bg="#c7ecee",activebackground="#636e72",command=lambda: click(2))
button_3 = Button(root,text="3",padx=58,font=("Bold",15),fg="Black",bg="#c7ecee",pady=25,activebackground="#636e72",command=lambda: click(3))
button_4 = Button(root,text="4",padx=63,font=("Bold",15),fg="Black",pady=25,bg="#c7ecee",activebackground="#636e72",command=lambda: click(4))
button_5 = Button(root,text="5",padx=58,font=("Bold",15),fg="Black",pady=25,bg="#c7ecee",activebackground="#636e72",command=lambda: click(5))
button_6 = Button(root,text="6",padx=58,font=("Bold",15),fg="Black",pady=25,bg="#c7ecee",activebackground="#636e72",command=lambda: click(6))
button_7 = Button(root,text="7",padx=63,font=("Bold",15),fg="Black",pady=25,bg="#c7ecee",activebackground="#636e72",command=lambda: click(7))
button_8 = Button(root,text="8",padx=58,font=("Bold",15),fg="Black",pady=25,bg="#c7ecee",activebackground="#636e72",command=lambda: click(8))
button_9 = Button(root,text="9",padx=58,font=("Bold",15),fg="Black",pady=25,bg="#c7ecee",activebackground="#636e72",command=lambda: click(9))
button_0 = Button(root,text="0",padx=63,font=("Bold",15),fg="Black",pady=25,bg="#c7ecee",activebackground="#636e72",command=lambda: click(0))


button_add = Button(root,text="+",font=("Bold",15),padx=58,pady=25,bg="#81ecec",activebackground="#00cec9",command=add)
button_sub = Button(root,text="-",font=("Bold",15),padx=59,pady=25,bg="#81ecec",activebackground="#00cec9",command=sub)
button_mult = Button(root,text="x",font=("Bold",15),padx=59,pady=25,bg="#81ecec",activebackground="#00cec9",command=mult)
button_div = Button(root,text="/",font=("Bold",15),padx=60,pady=25,bg="#81ecec",activebackground="#00cec9",command=div)

button_ac = Button(root,text="AC",padx=51,pady=25,font=("Bold",15),fg="Black",bg="#95afc0",activebackground="#2d3436",command=clear)
button_equal = Button(root,text="=",padx=58,pady=25,font=("Bold",15),bg="chartreuse2",activebackground="chartreuse4",command=equal)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_0.grid(row=4,column=0)
button_add.grid(row=4,column=2)
button_sub.grid(row=3,column=3)
button_ac.grid(row=4,column=1,rowspan=2)
button_mult.grid(row=2,column=3)
button_div.grid(row=1,column=3)
button_equal.grid(row=4,column=3)








root.mainloop()
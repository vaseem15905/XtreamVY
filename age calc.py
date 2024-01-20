from tkinter import*
from datetime import date
from tkinter import font


root=Tk()
root.geometry("440x400")
root.resizable(False,False)
root.title("Age Calculator")
root.config(bg="#94ffb4")


result_label = Label(root, text="", background="#bdf5ce", fg="#2a2526", font=("Berlin Sans FB", 25))

def calculateAge():
    today=date.today()
    birthDate=date(int(yearEntry.get()),int(monthEntry.get()),int(dayEntry.get()))
    age=today.year-birthDate.year-((today.month,today.day)<(birthDate.month,birthDate.day))
    result_label.config(text=f"{nameValue.get()}  your age is {age}")
    result_label.place(x=45, y=320)


def clear():
    nameValue.set('')
    yearValue.set('')
    monthValue.set('')
    dayValue.set('')
    result_label.place_forget()

Label(text="Name",font=("Berlin Sans FB",19),background="#94ffb4",fg="#2a2526").place(x=30,y=105)
Label(text="Day",font=("Berlin Sans FB",19),background="#94ffb4",fg="#2a2526").place(x=38,y=174)
Label(text="Month",font=("Berlin Sans FB",19),background="#94ffb4",fg="#2a2526").place(x=145,y=174)
Label(text="Year",font=("Berlin Sans FB",19),background="#94ffb4",fg="#2a2526").place(x=280,y=174)
Label(text="AGE CALCULATOR",font=("Courgette",30),background="#bdf5ce",fg="#2a2526").place(x=60,y=15)


nameValue=StringVar()
yearValue=StringVar()
monthValue=StringVar()
dayValue=StringVar()

nameEntry=Entry(root,textvariable=nameValue,background="#bdf5ce",width=19,bd=4,font=("Britannic",20))
nameEntry.place(x=110,y=100)

dayEntry=Entry(root,textvariable=dayValue,background="#bdf5ce",width=2,bd=4,font=("digital-7",21))
dayEntry.place(x=95,y=170)

monthEntry=Entry(root,textvariable=monthValue,background="#bdf5ce",width=2,bd=4,font=("digital-7",20))
monthEntry.place(x=224,y=170)

yearEntry=Entry(root,textvariable=yearValue,background="#bdf5ce",width=4,bd=4,font=("digital-7",20))
yearEntry.place(x=340,y=170)



Button(text="Calculate Age",font=("Berlin Sans FB",15),bg="#07923f",activebackground="#05662c",activeforeground="#d0fbdd",fg="#d0fbdd",width=17,bd=2,height=2,command=calculateAge).place(x=210,y=230)
Button(text="Clear",font=("Berlin Sans FB",15),bg="#16532e",activebackground="#0e341d",activeforeground="#d0fbdd",fg="#d0fbdd",width=6,bd=2,height=2,command=clear).place(x=110,y=230)
Button(text="Exit",font=("Berlin Sans FB",15),bg="#16532e",activebackground="#0e341d",activeforeground="#d0fbdd",fg="#d0fbdd",width=6,bd=2,height=2,command=lambda:root.destroy()).place(x=30,y=230)

root.mainloop()

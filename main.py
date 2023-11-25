from tkinter import*
    
root=Tk()
root.geometry("770x435")
root.title("Price Calculator")
root.config(bg="#6EC4D7")
root.resizable(0,0)


icon_image=PhotoImage(file="C:/Users/vasee/OneDrive/Desktop/workspace/Py Projects/PRICE CALCULATOR/logo.png")
root.iconphoto(False,icon_image)
       

def  reset1():
     amtentry.delete(0,END)
     Quantitytentry.delete(0,END)
     finalamt.config(text="")
     gbtn.config(image=grambtnimg)
     kgbtn.config(image=kgbtnimg)
     

def reset2():
    Quantitytentry.delete(0,END)
    finalamt.config(text="")
    kgbtn.config(image=kgbtnimg)
    gbtn.config(image=grambtnimg)

def kgcalc():
    amount=amt.get()
    quantity=quant.get()
    r=amount*quantity
    finalamt.config(text=r)
    kgbtn.config(image=activekgbtnimg)
    gbtn.config(image=grambtnimg)

def gcalc():
    amount=amt.get()
    quantity=quant.get()
    r=(amount*quantity)/1000
    finalamt.config(text=r)
    gbtn.config(image=activegrambtnimg)
    kgbtn.config(image=kgbtnimg)


img=PhotoImage(file="C:/Users/vasee/OneDrive/Desktop/workspace/Py Projects/PRICE CALCULATOR/Backround.png")
Label(root , image= img).pack()

amt=IntVar(value="")

amtentry=Entry(root,bg="#CCCCCC",textvariable=amt,width=6,borderwidth=0,selectbackground="#909090",selectforeground="black",font=("Digital-7",28))
amtentry.place(x=577,y=136)

quant=IntVar(value="")

Quantitytentry=Entry(root,bg="#CCCCCC",textvariable=quant,width=5,selectbackground="#909090",selectforeground="black",borderwidth=0,font=("Digital-7",28))
Quantitytentry.place(x=99,y=299)
       


finalamt=Label(root,bg="#CCCCCC",width=7,text="",activebackground="#909090",borderwidth=0,font=("Digital-7",30))
finalamt.place(x=518,y=296)

activegrambtnimg=PhotoImage(file="C:/Users/vasee/OneDrive/Desktop/workspace/Py Projects/PRICE CALCULATOR/activegrmimg.png")
grambtnimg=PhotoImage(file="C:/Users/vasee/OneDrive/Desktop/workspace/Py Projects/PRICE CALCULATOR/grambtn.png")
gbtn=Button(root,image=grambtnimg,borderwidth=0,bg="#6EC4D7",activebackground="#6EC4D7",command=gcalc)
gbtn.place(x=275,y=293)

activekgbtnimg=PhotoImage(file="C:/Users/vasee/OneDrive/Desktop/workspace/Py Projects/PRICE CALCULATOR/activekgimg.png")
kgbtnimg=PhotoImage(file="C:/Users/vasee/OneDrive/Desktop/workspace/Py Projects/PRICE CALCULATOR/kgbutton.png")
kgbtn=Button(root,image=kgbtnimg,borderwidth=0,bg="#6EC4D7",activebackground="#6EC4D7",command=kgcalc)
kgbtn.place(x=203,y=293)

resetnimg=PhotoImage(file="C:/Users/vasee/OneDrive/Desktop/workspace/Py Projects/PRICE CALCULATOR/resetbtn.png")


resetbtn1=Button(root,image=resetnimg,borderwidth=0,bg="#C994E3",activebackground="#C994E3",command=reset1)
resetbtn1.place(x=710,y=137,)

resetbtn2=Button(root,image=resetnimg,borderwidth=0,bg="#C994E3",activebackground="#C994E3",command=reset2)
resetbtn2.place(x=710,y=375,)    


    
root.mainloop()
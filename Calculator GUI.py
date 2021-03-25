import tkinter
from tkinter import *
from tkinter import messagebox

def add():
    v1 = val1.get()
    v2 = val2.get()
    ans = float(v1) + float(v2)
    result["text"]=str(ans)

def sub():
    v1 = val1.get()
    v2 = val2.get()
    ans = float(v1) - float(v2)
    result["text"]=str(ans)

def mul():
    v1 = val1.get()
    v2 = val2.get()
    ans = float(v1) * float(v2)
    result["text"]=str(ans)

def div():
    v1 = val1.get()
    v2 = val2.get()
    ans = float(v1) / float(v2)
    result["text"]=str(ans)

if __name__=="__main__":
    gui = Tk()
    gui.configure(background="hot pink1") #background color
    gui.title("Calculator") #title of GUI window
    gui.geometry("472x400") #window size

    #Heading
    dum0 = Label(gui,text="", bg="hot pink1", font=("Times", 20 ,"italic")) #dummy space
    var0 = Label(gui,text="Calculator", bg="hot pink1", font=("Times", 30 ,"italic"))
    dum1 = Label(gui,text="", bg="hot pink1", font=("Times", 20 ,"italic")) #dummy space

    #Enteries
    var1 = Label(gui, text="Enter first Value", bg="hot pink1",font=("Times",14,"bold")) #label
    val1 = Entry(gui,bg="lemon chiffon",width=20) #text
    var2 = Label(gui, text="Enter Second Value", bg="hot pink1", font=("Times",14,"bold")) #label
    val2 = Entry(gui,bg="lemon chiffon",width=20) #text

    #Buttons
    dum2 = Label(gui,text="",bg="hot pink1",font=("Times", 20 ,"italic")) #dummy space
    addition = Button(gui,text="+",height=2,width=4,font=("Times",14,"bold"),fg="Black",bg="cyan",command=add)
    subtraction = Button(gui,text="-",height=2,width=4,font=("times",14,"bold"),fg="Black",bg="cyan",command=sub)
    multiplication = Button(gui,text="x",height=2,width=4,font=("times",14,"bold"),fg="Black",bg="cyan",command=mul)
    division = Button(gui,text="/",height=2,width=4,font=("Times",14,"bold"),fg="Black",bg="cyan",command=div)
    dum3 = Label(gui,text="",bg="hot pink1",font=("Times", 20 ,"italic"))  #dummy space

    #result
    var3 = Label(gui, text="Result", bg="hot pink1",font=("Times",13,"bold")) #label
    result = Label(gui,height=1,width=20, font="lucida 13",bg="lemon chiffon")
    
    #Heading
    dum0.grid(row=1, column=1)
    var0.grid(row=2,column=2, columnspan=3)
    dum1.grid(row=4,column=1)

    #Enteries
    val1.grid(row=6, column=3)
    var1.grid(row=6, column=2)
    var2.grid(row=7, column=2)
    val2.grid(row=7, column=3)

    #Buttons
    dum2.grid(row=9,column=1)
    addition.grid(row=10,column=1,columnspan=1)
    subtraction.grid(row=10,column=2,columnspan=1)
    multiplication.grid(row=10, column=3,columnspan=1)
    division.grid(row=10,column=4,columnspan=1)
    dum3.grid(row=11,column=1)

    #Result
    var3.grid(row=13,column=2)
    result.grid(row=13, column=3)
    gui.mainloop()
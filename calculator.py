import tkinter
from tkinter import *
window = Tk()
window.title("CALCULATOR")

window.geometry("500x667")


OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"


def click(event):
    text=event.widget.cget("text")          
                        
    print(text)
    if text == "C":
        sval.set("")                        
        screen.update()
    elif text == "=":
        if sval.get().isdigit():            
            value=int(sval.get())           
        else:
            value=eval(screen.get())       

        sval.set(value)
        screen.update()
    elif text == "+/-":
        sval.get()
        sval.set(sval.get()*(-1))
        screen.update()
        
    else:
        sval.set(sval.get()+text)
        screen.update()  
    

sval = StringVar()
sval.set("")
screen= Entry(window,textvar=sval,font="lucida 35")
screen.pack(ipadx=8,pady=10,padx=10)


f1 = Frame(window, bg="black")

b = Button(f1, text="7", padx=28, pady=18, font="lucida 25 bold",activeforeground='red',activebackground="lightgrey")
b.pack(side=LEFT, padx=5, pady=2) #10,5
b.bind('<Button-1>', click)

b = Button(f1, text="8", padx=28, pady=18, font="lucida 25 bold",command=click)
b.pack(side=LEFT, padx=5, pady=2) #10,5
b.bind('<Button-1>', click)

b = Button(f1, text="9", padx=28, pady=18, font="lucida 25 bold")
b.pack(side=LEFT, padx=5, pady=2) #10,5
b.bind('<Button-1>', click)

b = Button(f1, text="*", padx=28, pady=18, font="lucida 25 bold")
b.pack(side=LEFT, padx=5, pady=2) #10,5
b.bind('<Button-1>', click)

f1.pack()

f1 = Frame(window, bg="black")

b = Button(f1, text="4", padx=28, pady=18, font="lucida 25 bold")
b.pack(side=LEFT, padx=5, pady=2) #10,5
b.bind('<Button-1>', click)

b = Button(f1, text="5", padx=28, pady=18, font="lucida 25 bold")
b.pack(side=LEFT, padx=5, pady=2)
b.bind('<Button-1>', click)

b = Button(f1, text="6", padx=28, pady=18, font="lucida 25 bold")
b.pack(side=LEFT, padx=5, pady=2) #10,5
b.bind('<Button-1>', click)

b = Button(f1, text="-", padx=33, pady=18, font="lucida 25 bold")
b.pack(side=LEFT, padx=5, pady=2) #10,5
b.bind('<Button-1>', click)

f1.pack()


f1 = Frame(window, bg="black")

b = Button(f1, text="1", padx=28, pady=18, font="lucida 25 bold")
b.pack(side=LEFT, padx=5, pady=2) #10,5
b.bind('<Button-1>', click)

b = Button(f1, text="2", padx=28, pady=18, font="lucida 25 bold")
b.pack(side=LEFT, padx=5, pady=2) #10,5
b.bind('<Button-1>', click)

b = Button(f1, text="3", padx=28, pady=18, font="lucida 25 bold")
b.pack(side=LEFT, padx=5, pady=2) #10,5
b.bind('<Button-1>', click)

b = Button(f1, text="+", padx=28, pady=18, font="lucida 25 bold")
b.pack(side=LEFT, padx=5, pady=2) #10,5
b.bind('<Button-1>', click)

f1.pack()


f1 = Frame(window, bg="black")

b = Button(f1, text="%", padx=21, pady=18, font="lucida 25 bold")
b.pack(side=LEFT, padx=5, pady=2) #10,5
b.bind('<Button-1>', click)

b = Button(f1, text="0", padx=28, pady=18, font="lucida 25 bold")
b.pack(side=LEFT, padx=5, pady=2) #10,5
b.bind('<Button-1>', click)

b = Button(f1, text=".", padx=28, pady=18, font="lucida 25 bold")
b.pack(side=LEFT, padx=5, pady=2) #10,5
b.bind('<Button-1>', click)

b = Button(f1, text="=", padx=28, pady=18, font="lucida 25 bold")
b.pack(side=LEFT, padx=5, pady=2) #10,5
b.bind('<Button-1>', click)

f1.pack()
window.mainloop()

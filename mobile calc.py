from tkinter import *
import math
box=Tk()
box.title('Calculator')
box.minsize(width=400,height=350)
box.maxsize(width=600,height=600)
boxlabel = Label(box,text="CALCULATOR",bg='dark gray',font=("Times",30,'bold'))
boxlabel.pack(side=TOP)
box.config(background='Dark gray')

textin=StringVar()
operator=""

def clickbut(number):   #lambda:clickbut(1)
     global operator
     temp =operator
     if number=="^":# for chceking the power of a given number
         temp=operator+str(number)
         textin.set(temp)
         operator=operator+str("**")
     else:
         operator=operator+str(number)
         textin.set(operator)

def equlbut():
     global operator
     add=str(eval(operator))
     textin.set(add)
     operator=''
def equlbut():
     global operator
     sub=str(eval(operator))
     textin.set(sub)
     operator=''     
def equlbut():
     global operator
     mul=str(eval(operator))
     textin.set(mul)
     operator=''
def equlbut():
     global operator
     div=str(eval(operator))
     textin.set(div)
     operator=''
def equlbut():
     global operator
     mod=str(eval(operator))
     textin.set(mod)
     operator=''    
def sqrt():
    global operator
    a=float(textin.get())
    b=math.sqrt(a)
    textin.set(b)
    operator= str(b)
def pow():
   global operator
   print(operator)
   pow=str(eval(operator))
   textin.set(pow)
   operator=""

def clrbut():
    global operator
    operator=''
    textin.set('')
   



b1=Entry(box,textvar=textin)
b1.place(x=00,y=50,width=400,height=30)
b2=Button(box,text="C",command=clrbut,width=5,height=2)
b2.place(x=00,y=100)
b3=Button(box,command=lambda:clickbut("^"),text="Power",width=5,height=2)
b3.place(x=100,y=100)
b4=Button(box,command=lambda:clickbut("%"),text="%",width=5,height=2)
b4.place(x=200,y=100)
b5=Button(box,command=lambda:clickbut("/"),text="/",width=5,height=2)
b5.place(x=300,y=100)
b6=Button(box,command=lambda:clickbut(7),text="7",width=5,height=2)
b6.place(x=00,y=150)
b7=Button(box,command=lambda:clickbut(8),text="8",width=5,height=2)
b7.place(x=100,y=150)
b8=Button(box,command=lambda:clickbut(9),text="9",width=5,height=2)
b8.place(x=200,y=150)
b9=Button(box,command=lambda:clickbut("*"),text="*",width=5,height=2)
b9.place(x=300,y=150)
b10=Button(box,command=lambda:clickbut(4),text="4",width=5,height=2)
b10.place(x=00,y=200)
b11=Button(box,command=lambda:clickbut(5),text="5",width=5,height=2)
b11.place(x=100,y=200)
b12=Button(box,command=lambda:clickbut(6),text="6",width=5,height=2)
b12.place(x=200,y=200)
b13=Button(box,command=lambda:clickbut("-"),text="-",width=5,height=2)
b13.place(x=300,y=200)
b14=Button(box,command=lambda:clickbut(1),text="1",width=5,height=2)
b14.place(x=00,y=250)
b15=Button(box,command=lambda:clickbut(2),text="2",width=5,height=2)
b15.place(x=100,y=250)
b16=Button(box,command=lambda:clickbut(3),text="3",width=5,height=2)
b16.place(x=200,y=250)
b17=Button(box,command=lambda:clickbut("+"),text="+",width=5,height=2)
b17.place(x=300,y=250)
b18=Button(box,command=sqrt,text="sqrt",width=5,height=2)
b18.place(x=00,y=300)
b19=Button(box,command=lambda:clickbut("0"),text="0",width=5,height=2)
b19.place(x=100,y=300)
b20=Button(box,command=lambda:clickbut("0"),text="0",width=5,height=2)
b20.place(x=100,y=300)
b21=Button(box,command=lambda:clickbut("."),text=".",width=5,height=2)
b21.place(x=200,y=300)
b22=Button(box,text="=",command=equlbut,width=5,height=2)
b22.place(x=300,y=300)
box.mainloop()

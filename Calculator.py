from tkinter import*
from math import*
#-------Create-Func----------
#--------Clavier----------    
def setnum(num):
    global exp
    exp= exp + str(num)
    x.set(exp)
def clear():
    global exp 
    exp = ' '
    x.set(exp)
def calculator():
    try: 
        global exp
        output= str(eval(exp))
        x.set(output)
    except: 
        x.set("Error")
        exp = " "
def Label_func1():
    Func_Afficheur['text']='RAD'



#-------Create-Window--------
win= Tk()
win.title('Calculatrice')
win.minsize(320,600)
win.maxsize(320,600)
win.config(background='#474545')
win.iconbitmap('.../Calculator/Calculator-icon.ico')
#--------Create-Objects-------
#-------Variables -----------
exp= ' '
x=StringVar()
#--------Create-Frame---------
theTop_frame=Frame(win,width=320,height=100,bg='#3A3A3A')
Bottom_frame=Frame(win,width=320,height=380,bg='#474545')
#--------Create-Label---------
Func_Afficheur= Label(theTop_frame,text='RAD',bg='#3A3A3A',width=80,height=2,font=('Courier','16'),bd='0',anchor=NW,padx=5,pady=5,fg='#DCDBDB')
Afficheur=Entry(theTop_frame,state=NORMAL,disabledbackground='#3A3A3A',bd='0',width=320,font=('Courier','35'),justify=RIGHT,textvariable=x)
Afficheur.config(background='#3A3A3A')
Afficheur.pack(expand=YES)
Func_Afficheur.pack(side=LEFT,expand=YES,fill=BOTH)
#--------Create-Button--------
btn1= Button(Bottom_frame,text='RAD',command=Label_func1,width=10,height=2,bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0')
btn3= Button(Bottom_frame,text='π',command=lambda : setnum('pi'),width=10,height=2,bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0')
btn4= Button(Bottom_frame,text='| x |',command=lambda: setnum('abs'),width=10,height=2,bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0')
btn5= Button(Bottom_frame,text='sin',command=lambda: setnum('sin'),width=10,height=2,bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0')
btn6= Button(Bottom_frame,text='cos',command=lambda: setnum('cos'),width=10,height=2,bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0')
btn7= Button(Bottom_frame,text='tan',command=lambda: setnum('tan'),width=10,height=2,bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0')
btn8= Button(Bottom_frame,text='AC',command=clear,width=10,height=2,bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0')
btn9= Button(Bottom_frame,text='xʸ',command=lambda: setnum('**'),width=10,height=2,bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0')
btn10= Button(Bottom_frame,text='(',command=lambda: setnum('('),width=10,height=2,bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0')
btn11= Button(Bottom_frame,text=')',command=lambda: setnum(')'),width=10,height=2,bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0')
btn12= Button(Bottom_frame,text='÷',command= lambda: setnum('/'),width=10,height=2,bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0')
btn13= Button(Bottom_frame,text='1',command=lambda: setnum('1'),width=10,height=2,bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0')
btn14= Button(Bottom_frame,text='2',command=lambda: setnum('2'),width=10,height=2,bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0')
btn15= Button(Bottom_frame,text='3',command=lambda: setnum('3'),width=10,height=2,bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0')
btn16= Button(Bottom_frame,text='4',command=lambda: setnum('4'),width=10,height=2,bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0')
btn17=Button(Bottom_frame,text='5',command=lambda: setnum('5'),width=10,height=2,bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0')
btn18=Button(Bottom_frame,text='6',command=lambda: setnum('6'),width=10,height=2,bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0')
btn19=Button(Bottom_frame,text='-',command=lambda: setnum('-'),width=10,height=2,bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0')
btn20=Button(Bottom_frame,text='7',command=lambda: setnum('7'),width=10,height=2,bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0')
btn21=Button(Bottom_frame,text='8',command=lambda: setnum('8'),width=10,height=2,bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0')
btn22=Button(Bottom_frame,text='9',command=lambda: setnum('9'),width=10,height=2,bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0')
btn23=Button(Bottom_frame,text='×',command=lambda: setnum('*'),width=10,height=2,bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0')
btn24=Button(Bottom_frame,text='+',command=lambda: setnum('+'),width=10,height=2,bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0')
btn25=Button(Bottom_frame,text='√',command=lambda: setnum('sqrt') ,width=10,height=2,bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0')
btn26=Button(Bottom_frame,text='0',command=lambda: setnum('0'),width=10,height=2,bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0')
btn27=Button(Bottom_frame,text='.',command=lambda: setnum('.'),width=10,height=2,bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0')
btn28=Button(Bottom_frame,text='=',command=calculator,width=10,height=2,bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0')
#------Programme-Principale---
#------Placing-Buttons--------
#------Column 1-------
btn1.place(x=1,y=1)
btn3.place(x=159,y=1)
btn4.place(x=238,y=1)
#------Column 2-------
btn5.place(x=1,y=51)
btn6.place(x=80,y=51)
btn7.place(x=159,y=51)
btn8.place(x=238,y=51)
#------Column 3-------
btn9.place(x=1,y=101)
btn10.place(x=80,y=101)
btn11.place(x=159,y=101)
btn12.place(x=238,y=101)
#------Column 4-------
btn13.place(x=1,y=151)
btn14.place(x=80,y=151)
btn15.place(x=159,y=151)
btn23.place(x=238,y=151)
#------Column 5-------
btn16.place(x=1,y=201)
btn17.place(x=80,y=201)
btn18.place(x=159,y=201)
btn19.place(x=238,y=201)
#------Column 6-------
btn20.place(x=1,y=251)
btn21.place(x=80,y=251)
btn22.place(x=159,y=251)
btn24.place(x=238,y=251)
#------Column 7-------
btn25.place(x=1,y=301)
btn26.place(x=80,y=301)
btn27.place(x=159,y=301)
btn28.place(x=238,y=301)


theTop_frame.pack(side=TOP)
Bottom_frame.pack(side=BOTTOM)
win.mainloop()
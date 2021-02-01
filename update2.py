#  Calculator -----------------------------------------------------------------------------------------------

import tkinter as tk
rw = tk.Tk()
rw.title('Calculator')
rw.geometry('305x400+300+100')

fm1 = tk.Frame(master = rw, height = 400, width=305, bg = 'black')
fm1.pack()
add,add1 = (0,0)
# Functions Area ------------------------------------------------------------------------------------------

def delete():
    x = en2.get()
    en2.delete(len(x)-1,tk.END)

def ce():
    en2.delete(0,tk.END)
    lb1 = tk.Label(fm1,text = '',bg = 'black',fg = 'white',bd = 1,width = 15, font = ('Arial,Italic',25)).place(x = 7, y = 20)

def sign(s):
    en2.insert(0,s)


def eq(): 
    x = en2.get() 
    lb1 = tk.Label(fm1,text = str(eval(x)),bg = 'black',fg = 'white',bd = 1,width = 15, font = ('Arial,Italic',25)).place(x = 7, y = 20)
    add = add + 1
    add1 = add1 + 1

def btn_clk(number):
#     en2.insert(tk.END,number)
    print(add)
    print(add1)
    if add == add1:
        
        en2.insert(tk.END,number)
    else:
        en2.delete(0,tk.END)
        en2.insert(tk.END,number) 
        add1 = add1 + 1

    
# Last row '+/-' , '0','.','='----------------------------------------------------------------------------
# > '+/-'
btpm = tk.Button(master = fm1, text = "+/-", bg = 'black',fg = 'white',
                activeforeground = 'black', activebackground = 'gray' ,
                bd = None , height = 3, width = 9, command = lambda : sign('-'))
btpm.place(x= 2,y = 340)

# > '0'
bt0 = tk.Button(master = fm1, text = "0", bg = 'black',fg = 'white',
                activeforeground = 'black', activebackground = 'gray' , 
                bd = None , height = 3, width = 9, command = lambda : btn_clk(0))
bt0.place(x= 77,y = 340)

# > '.'
btdt = tk.Button(master = fm1, text = ".\n(dot)", bg = 'black',fg = 'white',
                activeforeground = 'black', activebackground = 'gray' , 
                bd = None , height = 3, width = 9,command = lambda : btn_clk('.'))
btdt.place(x= 152,y = 340)

# > '='
bteq = tk.Button(master = fm1, text = "=", bg = 'lightblue',fg = 'black',
                activeforeground = 'white', activebackground = 'blue' , 
                bd = 1, height = 3, width = 9, command = eq)
bteq.place(x= 228,y = 340)


# Second row '1','2','3','+'----------------------------------------------------------

# > '1'
bt1 = tk.Button(master = fm1, text = "1", bg = 'black',fg = 'white',
                activeforeground = 'black', activebackground = 'gray' ,
                bd = None , height = 3, width = 9, command = lambda : btn_clk(1))
bt1.place(x= 2,y = 282)

# > '2'
bt2 = tk.Button(master = fm1, text = "2", bg = 'black',fg = 'white',
                activeforeground = 'black', activebackground = 'gray' , 
                bd = None , height = 3, width = 9, command = lambda : btn_clk(2))
bt2.place(x= 77,y = 282)

# > '3'
bt3 = tk.Button(master = fm1, text = "3", bg = 'black',fg = 'white',
                activeforeground = 'black', activebackground = 'gray' , 
                bd = None , height = 3, width = 9, command = lambda : btn_clk(3))
bt3.place(x= 152,y = 282)

# > '+'
btpls = tk.Button(master = fm1, text = "+", bg = 'gray',fg = 'black',
                activeforeground = 'white', activebackground = 'black' , 
                bd = None , height = 3, width = 9, command = lambda : btn_clk('+'))
btpls.place(x= 228,y = 282)

# # Third row '4','5','6','-'----------------------------------------------------------

# > '4'
bt4 = tk.Button(master = fm1, text = "4", bg = 'black',fg = 'white',
                activeforeground = 'black', activebackground = 'gray' ,
                bd = None , height = 3, width = 9, command = lambda : btn_clk(4))
bt4.place(x= 2,y = 224)

# > '5'
bt5 = tk.Button(master = fm1, text = "5", bg = 'black',fg = 'white',
                activeforeground = 'black', activebackground = 'gray' , 
                bd = None , height = 3, width = 9, command = lambda : btn_clk(5))
bt5.place(x= 77,y = 224)

# > '6'
bt6 = tk.Button(master = fm1, text = "6", bg = 'black',fg = 'white',
                activeforeground = 'black', activebackground = 'gray' , 
                bd = None , height = 3, width = 9, command = lambda : btn_clk(6))
bt6.place(x= 152,y = 224)

# > '-'
btmns = tk.Button(master = fm1, text = "-", bg = 'gray',fg = 'black',
                activeforeground = 'white', activebackground = 'black', 
                bd = None , height = 3, width = 9, command = lambda : btn_clk('-'))
btmns.place(x= 228,y = 224)

# Forth row '7','8','9','x'----------------------------------------------------------

# > '7'
bt7 = tk.Button(master = fm1, text = "7", bg = 'black',fg = 'white',
                activeforeground = 'black', activebackground = 'gray' ,
                bd = None , height = 3, width = 9, command = lambda : btn_clk(7))
bt7.place(x= 2,y = 166)

# > '8'
bt8 = tk.Button(master = fm1, text = "8", bg = 'black',fg = 'white',
                activeforeground = 'black', activebackground = 'gray' , 
                bd = None , height = 3, width = 9, command = lambda : btn_clk(8))
bt8.place(x= 77,y = 166)

# > '9'
bt9 = tk.Button(master = fm1, text = "9", bg = 'black',fg = 'white',
                activeforeground = 'black', activebackground = 'gray' , 
                bd = None , height = 3, width = 9, command = lambda : btn_clk(9))
bt9.place(x= 152,y = 166)

# > 'x'
btmul = tk.Button(master = fm1, text = "x", bg = 'gray',fg = 'black',
                activeforeground = 'white', activebackground = 'black', 
                bd = None , height = 3, width = 9, command = lambda : btn_clk('*'))
btmul.place(x= 228,y = 166)


# Last Fifth row 'CE','C','DEL','÷'----------------------------------------------------------

# > 'CE'
btce = tk.Button(master = fm1, text = "CE", bg = 'gray',fg = 'black',
                activeforeground = 'white', activebackground = 'black',
                bd = None , height = 2, width = 9, command = ce)
btce.place(x= 2,y = 123)

# > 'C'
btc = tk.Button(master = fm1, text = "C", bg = 'gray',fg = 'black',
                activeforeground = 'white', activebackground = 'black', 
                bd = None , height = 2, width = 9, command = ce)
btc.place(x= 77,y = 123)

# > 'DEL'
btdel = tk.Button(master = fm1, text = "DEL", bg = 'gray',fg = 'black',
                activeforeground = 'white', activebackground = 'black', 
                bd = None , height = 2, width = 9, command = delete)
btdel.place(x= 152,y = 123)

# > '÷'
btdiv = tk.Button(master = fm1, text = "÷", bg = 'gray',fg = 'black',
                  activeforeground = 'white', activebackground = 'black', 
                  bd = None , height = 2, width = 9, command = lambda : btn_clk('/'))
btdiv.place(x= 228,y = 123)

# Entry Box ------------------------------------------------------------------------------------------

en2 = tk.Entry(fm1,bg = 'black',fg = 'white',bd = 0,width = 16, font = ('Arial,Bold',25), justify = 'right')
en2.place(x= 7, y = 70)

rw.mainloop()

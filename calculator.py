from tkinter import *

def btnClick(number):
    global operator
    operator = operator + str(number)
    text_input.set(operator)

def btnClear():
    global operator
    operator=""
    text_input.set("")

def btnEquals():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=""
    

cal = Tk()
cal.title("Standard Calculator")
cal.configure(background="powder blue")
operator = ""
text_input = StringVar()

txtDisplay = Entry(cal, font=('arial',20,'bold'),textvariable=text_input, bd=30, insertwidth=4, bg="powder blue", justify="right").grid(columnspan=4)


btn7 = Button(cal,padx=16, pady=16, command=lambda:btnClick(7), bd=8, bg="powder blue", fg="black", font=('arial',20,'bold'), text="7").grid(row=1,column=0)
btn8 = Button(cal,padx=16, pady=16, command=lambda:btnClick(8), bd=8, bg="powder blue", fg="black", font=('arial',20,'bold'), text="8").grid(row=1,column=1)
btn9 = Button(cal,padx=16, pady=16, command=lambda:btnClick(9), bd=8, bg="powder blue", fg="black", font=('arial',20,'bold'), text="9").grid(row=1,column=2)
Addition = Button(cal,padx=16, pady=16, command=lambda:btnClick("+"), bd=8, bg="powder blue", fg="black", font=('arial',20,'bold'), text="+").grid(row=1,column=3)

btn4 = Button(cal,padx=16,bd=8, pady=16, command=lambda:btnClick(4), bg="powder blue", fg="black", font=('arial',20,'bold'), text="4").grid(row=2,column=0)
btn5 = Button(cal,padx=16,bd=8, pady=16, command=lambda:btnClick(5), bg="powder blue", fg="black", font=('arial',20,'bold'), text="5").grid(row=2,column=1)
btn6 = Button(cal,padx=16,bd=8, pady=16, command=lambda:btnClick(6), bg="powder blue", fg="black", font=('arial',20,'bold'), text="6").grid(row=2,column=2)
Subtraction = Button(cal,padx=16, pady=16, command=lambda:btnClick("-"), bd=8, bg="powder blue", fg="black", font=('arial',20,'bold'), text="-").grid(row=2,column=3)

btn1 = Button(cal,padx=16,bd=8, pady=16, command=lambda:btnClick(1), bg="powder blue", fg="black", font=('arial',20,'bold'), text="1").grid(row=3,column=0)
btn2 = Button(cal,padx=16,bd=8, pady=16, command=lambda:btnClick(2), bg="powder blue", fg="black", font=('arial',20,'bold'), text="2").grid(row=3,column=1)
btn3 = Button(cal,padx=16,bd=8, pady=16, command=lambda:btnClick(3), bg="powder blue", fg="black", font=('arial',20,'bold'), text="3").grid(row=3,column=2)
Multiplication = Button(cal,padx=16, pady=16, command=lambda:btnClick("*"), bd=8, bg="powder blue", fg="black", font=('arial',20,'bold'), text="*").grid(row=3,column=3)

btn0 = Button(cal,padx=16, pady=16, bd=8, bg="powder blue", fg="black", font=('arial',20,'bold'), text="0").grid(row=4,column=0)
btnC = Button(cal,padx=16, pady=16, bd=8, command=btnClear,  bg="powder blue", fg="black", font=('arial',20,'bold'), text="C").grid(row=4,column=1)
btnEQ = Button(cal,padx=16, pady=16, bd=8, command=btnEquals, bg="powder blue", fg="black", font=('arial',20,'bold'), text="=").grid(row=4,column=2)
Divide = Button(cal,padx=16, pady=16, bd=8, command=lambda:btnClick("/"), bg="powder blue", fg="black", font=('arial',20,'bold'), text="/").grid(row=4,column=3)

cal.mainloop()

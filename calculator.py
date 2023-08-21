from tkinter import *
import math

exp = ''


def press(num):
    global exp

    equation.set(num)
    exp = exp + str(num)


def pressequal():
    try:
        global exp
        total = str(eval(exp))
        equation.set(total)
        exp = ""


    except:

        equation.set("error")
        exp = ""


def clear():
    global exp
    exp = ""
    equation.set(exp)


if __name__ == "__main__":
    w = Tk()
    w.title("Calculator")
    w.geometry("400x400")
    equation = StringVar()
    entry = Entry(w, textvariable=equation, font=('left', 20))
    entry.place(x=50, y=2)

    b1 = Button(w, text="c", font=('Arial', 15), width=3, command=clear)

    b2 = Button(w, text="√", font=('Arial', 15), width=3,
                command=lambda: press('√'), height=1)

    b3 = Button(w, text='/', font=('Arial', 15), width=3,
                command=lambda: press("/"), height=1)

    b4 = Button(w, text='<-', font=('Arial', 15), width=3,
                command=lambda: press("<-"), height=1)

    b5 = Button(w, text='7', font=('Arial', 15), width=3,
                command=lambda: press(7), height=1)

    b6 = Button(w, text='8', font=('Arial', 15), width=3,
                command=lambda: press(6), height=1)

    b7 = Button(w, text='9', font=('Arial', 15), width=3, command=
    lambda: press(5), height=1)

    b8 = Button(w, text='*', font=('Arial', 15), width=3,
                command=lambda: press("*"), height=1)

    b9 = Button(w, text='4', font=('Arial', 15), width=3,
                command=lambda: press(4), height=1)

    b10 = Button(w, text='5', font=('Arial', 15), width=3, command=
    lambda: press(5), height=1)

    b11 = Button(w, text='6', font=('Arial', 15), width=3,
                 command=lambda: press(6), height=1)

    b12 = Button(w, text='-', font=('Arial', 15), width=3,
                 command=lambda: press("-"), height=1)

    b13 = Button(w, text='1', font=('Arial', 15), width=3,
                 command=lambda: press(1), height=1)

    b14 = Button(w, text='2', font=('Arial', 15), width=3,
                 command=lambda: press(2), height=1)

    b15 = Button(w, text='3', font=('Arial', 15), width=3,
                 command=lambda: press(3), height=1)

    b16 = Button(w, text='+', font=('Arial', 15), width=3,
                 command=lambda: press("+"), height=1)

    b17 = Button(w, text='!', font=('Arial', 15), width=3,
                 command=lambda: press("!"), height=1)

    b18 = Button(w, text='0', font=('Arial', 15), width=3,
                 command=lambda: press(0), height=1)

    b19 = Button(w, text='.', font=('Arial', 15), width=3,
                 command=lambda: press("."), height=1)

    b20 = Button(w, text='=', font=('Arial', 15), width=3, command=pressequal)

    b1.place(x=50, y=50)
    b2.place(x=140, y=50)
    b3.place(x=220, y=50)
    b4.place(x=300, y=50)
    b5.place(x=50, y=100)
    b6.place(x=140, y=100)
    b7.place(x=220, y=100)
    b8.place(x=300, y=100)
    b9.place(x=50, y=150)
    b10.place(x=140, y=150)
    b11.place(x=220, y=150)
    b12.place(x=300, y=150)
    b13.place(x=50, y=200)
    b14.place(x=140, y=200)
    b15.place(x=220, y=200)
    b16.place(x=300, y=200)
    b17.place(x=50, y=250)
    b18.place(x=140, y=250)
    b19.place(x=220, y=250)
    b20.place(x=300, y=250)
    w.mainloop()



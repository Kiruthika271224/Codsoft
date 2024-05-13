from tkinter import Button, END, Text, Tk
import re
from math import sqrt

root = Tk()
root.title("Calculator")
root.geometry("375x400+450+50")
root.configure(bg="grey")
root.resizable(width=0, height=0)

entry = Text(root, width=37, height=3, bg="white", bd=10, font=("Arial", 12))
entry.place(x=10, y=10)

def calculate():
    get_all = entry.get(1.0, END)
    value = get_all
    value = re.sub(u"\u00F7", "/", value)
    value = re.sub("X", "*", value)
    value = re.sub("%", "/100", value)
    answer = eval(value)
    entry.delete(1.0, END)
    entry.insert(1.0, answer)

def clear():
    entry.delete(1.0, END)

def buttons(text):
    entry.insert(END, text)

def squareroot():
    get_all = entry.get(1.0, END)
    value = get_all
    answer = sqrt(int(value))
    entry.delete(1.0, END)
    entry.insert(1.0, answer)

def all_buttons():
    button_nine = Button(root, text="9", width=8, height=2, bd=5,
                         font=("Arial", 12), bg="grey", command=lambda: buttons("9"))
    button_nine.place(x=190, y=160)
    button_eight = Button(root, text="8", width=8, height=2, bd=5,
                          font=("Arial", 12), bg="grey", command=lambda: buttons("8"))
    button_eight.place(x=100, y=160)
    button_seven = Button(root, text="7", width=8, height=2, bd=5,
                          font=("Arial", 12), bg="grey", command=lambda: buttons("7"))
    button_seven.place(x=10, y=160)
    button_six = Button(root, text="6", width=8, height=2, bd=5,
                        font=("Arial", 12), bg="grey", command=lambda: buttons("6"))
    button_six.place(x=190, y=220)
    button_five = Button(root, text="5", width=8, height=2, bd=5,
                         font=("Arial", 12), bg="grey", command=lambda: buttons("5"))
    button_five.place(x=100, y=220)
    button_four = Button(root, text="4", width=8, height=2, bd=5,
                         font=("Arial", 12), bg="grey", command=lambda: buttons("4"))
    button_four.place(x=10, y=220)
    button_three = Button(root, text="3", width=8, height=2, bd=5,
                          font=("Arial", 12), bg="grey", command=lambda: buttons("3"))
    button_three.place(x=190, y=280)
    button_two = Button(root, text="2", width=8, height=2, bd=5,
                        font=("Arial", 12), bg="grey", command=lambda: buttons("2"))
    button_two.place(x=100, y=280)
    button_one = Button(root, text="1", width=8, height=2, bd=5,
                        font=("Arial", 12), bg="grey", command=lambda: buttons("1"))
    button_one.place(x=10, y=280)
    button_zero = Button(root, text="0", width=8, height=2, bd=5,
                         font=("Arial", 12), bg="grey", command=lambda: buttons("0"))
    button_zero.place(x=10, y=340)
    button_dot = Button(root, text=".", width=8, height=2, bd=5,
                        font=("Arial", 12), bg="dark orange", command=lambda: buttons("."))
    button_dot.place(x=190, y=340)
    button_plus = Button(root, text="+", width=8, height=2, bd=5,
                         font=("Arial", 12), bg="dark orange", command=lambda: buttons("+"))
    button_plus.place(x=280, y=100)
    button_minus = Button(root, text="-", width=8, height=2, bd=5,
                          font=("Arial", 12), bg="dark orange", command=lambda: buttons("-"))
    button_minus.place(x=280, y=160)
    button_div = Button(root, text=u"\u00F7", width=8, height=2, bd=5,
                        font=("Arial", 12), bg="dark orange", command=lambda: buttons(u"\u00F7"))
    button_div.place(x=280, y=220)
    button_multi = Button(root, text="X", width=8, height=2, bd=5,
                          font=("Arial", 12), bg="dark orange", command=lambda: buttons("X"))
    button_multi.place(x=280, y=280)
    button_squareroot = Button(root, text=u'\u221a', width=8, height=2, bd=5,
                               font=("Arial", 12), bg="dark orange", command=lambda: squareroot())
    button_squareroot.place(x=100, y=340)
    button_percent = Button(root, text="%", width=8, height=2, bd=5,
                            font=("Arial", 12), bg="dark orange", command=lambda: buttons("%"))
    button_percent.place(x=190, y=100)
    button_clear = Button(root, text="C", width=18, height=2, bd=5,
                          font=("Arial", 12), bg="light blue", command=lambda: clear())
    button_clear.place(x=10, y=100)
    button_calc = Button(root, text="=", width=8, height=2, bd=5,
                         font=("Arial", 12), bg="#ff6500", command=calculate)
    button_calc.place(x=280, y=340)

all_buttons()

root.mainloop()
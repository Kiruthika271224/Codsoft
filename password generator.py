from tkinter import *
import random

root = Tk()
root.title("Password Generator")
root.geometry("400x230")
root.configure(bg="indigo")
passstr = StringVar()
passlen = IntVar()
passlen.set(0)
username = StringVar()

def generate():
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', 
            '*', '(', ')']
    password = ""
    for x in range(passlen.get()):
        password = password + random.choice(pass1)
    passstr.set(password)

Label(root, text="Password Generator", font="calibri 20 bold",bg="indigo",fg="white").pack()
Label(root, text="Enter your name:" ,width=20).pack(pady=3)
Entry(root, textvariable=username).pack(pady=3)
Label(root, text="Enter password length:" ,width=20).pack(pady=3)
Entry(root, textvariable=passlen).pack(pady=3)
Button(root, text="Generate Password", command=generate,width=20).pack(pady=7)
Entry(root, textvariable=passstr).pack(pady=3)
root.mainloop()
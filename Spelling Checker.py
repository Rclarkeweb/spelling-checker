# Spelling Checker GUI using Tkinter

import tkinter
from tkinter import *
from textblob import TextBlob

root = Tk ()
root.title("Spelling Checker")
root.geometry("650x400")
root.config(background = "#f6f4d2")
def check_spelling():
    word = enter_text.get()
    a = TextBlob (word)
    right = str(a.correct())

    cs = Label(root, text = "Correct text is :", font=("Poppins", 20),bg="#f6f4d2", fg = "#386641")
    cs.place(x=100, y=290)
    spell.config(text=right)
    
heading = Label(root, text = "Spelling Checker", font = ("Poppins", 20, "bold"), bg="#f6f4d2", fg = "#386641")
heading.pack(pady = (50,0))
enter_text = Entry(root, justify="center", width=30, font=("Poppins", 18, "bold"), bg="white", border=2)
enter_text.pack(pady=10)
enter_text.focus()

Button=Button(root, text = "Check my spelling", width=20, font=("Poppins", 14, "bold"), fg="white", bg="#6a994e",command=check_spelling)
Button.pack(pady=(10))

spell = Label(root,font=("Poppins", 20), bg= "#f6f4d2", fg="#386641")
spell.place(x=350, y=290)
root.mainloop()
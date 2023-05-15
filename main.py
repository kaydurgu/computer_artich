from tkinter import *
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from sympy.logic.boolalg import simplify_logic

def simplify_expression(expr_string):
    expr = parse_expr(expr_string)

    simplified_expr = simplify_logic(expr)

    return str(simplified_expr)

def button_click():
    expr_string = entry.get()

    simplified_expr = simplify_expression(expr_string)

    label.config(text=simplified_expr)

window = Tk()
window.title("Boolean Expression Simplifier")

entry = Entry(window, width=50)
entry.pack()

button = Button(window, text="Simplify", command=button_click)
button.pack()

label = Label(window, text="")
label.pack()

window.mainloop()

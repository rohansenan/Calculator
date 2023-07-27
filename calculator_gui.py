
from tkinter import *
from tkinter import messagebox
from tkmacosx import Button
from calculator_operations import *

window = Tk()
window.title("calculator")
window.geometry('329x404')
calc = Calc()
output = StringVar(window)
output.set("0")

for i in range(4):
    Grid.columnconfigure(window, i, weight=1)
    Grid.rowconfigure(window, i, weight=1)
Grid.rowconfigure(window, 4, weight=1)
Grid.rowconfigure(window, 5, weight=1)

#define buttons, labels and messagebox
answer = Label(window, textvariable=output, background='Black')
clear = Button(window, text = "C", command=lambda: clicked("clear"), bg='darkgrey', activebackground='grey')
decimal_button = Button(window, text = ".", command=lambda: clicked("decimal"))
equal_button = Button(window, text = "=", command=lambda: clicked("equal"), bg='Orange')
delete = Button(window, command=lambda: clicked("delete"))
b0 = Button(window, text = 0, command=lambda: clicked("0"))
b1 = Button(window, text = 1, command=lambda: clicked("1"))
b2 = Button(window, text = 2, command=lambda: clicked("2"))
b3 = Button(window, text = 3, command=lambda: clicked("3"))
b4 = Button(window, text = 4, command=lambda: clicked("4"))
b5 = Button(window, text = 5, command=lambda: clicked("5"))
b6 = Button(window, text = 6, command=lambda: clicked("6"))
b7 = Button(window, text = 7, command=lambda: clicked("7"))
b8 = Button(window, text = 8, command=lambda: clicked("8"))
b9 = Button(window, text = 9, command=lambda: clicked("9"))
divide_button = Button(window, text = "/", command=lambda: clicked("division"), bg='Orange')
multiply_button = Button(window, text = "X", command=lambda: clicked("multiplication"), bg='Orange')
subtract_button = Button(window, text = "-", command=lambda: clicked("subtraction"), bg='Orange')
add_button = Button(window, text = "+", command=lambda: clicked("addition"), bg='Orange')
exponent_button = Button(window, text = "^", command=lambda: clicked("exponent"), bg='Orange')
root_button = Button(window, text = "√", command=lambda: clicked("root"), bg='Orange')
change_sign_button = Button(window, text = "+/-", command=lambda: clicked("change sign"), bg='Orange')

#place buttons
answer.grid(row=0, column=0, columnspan=4, sticky=NSEW)
clear.grid(row=5, column=0, sticky=NSEW)
decimal_button.grid(row=5, column=2, sticky=NSEW)
equal_button.grid(row=5, column=3, sticky=NSEW)  
b0.grid(row=5, column=1, sticky=NSEW)
b1.grid(row=2, column=0, sticky=NSEW)
b2.grid(row=2, column=1, sticky=NSEW)
b3.grid(row=2, column=2, sticky=NSEW)
b4.grid(row=3, column=0, sticky=NSEW)
b5.grid(row=3, column=1, sticky=NSEW)
b6.grid(row=3, column=2, sticky=NSEW)
b7.grid(row=4, column=0, sticky=NSEW)
b8.grid(row=4, column=1, sticky=NSEW)
b9.grid(row=4, column=2, sticky=NSEW)
divide_button.grid(row=1, column=3, sticky=NSEW)
multiply_button.grid(row=2, column=3, sticky=NSEW)
subtract_button.grid(row=3, column=3, sticky=NSEW)
add_button.grid(row=4, column=3, sticky=NSEW)
exponent_button.grid(row=1, column=1, sticky=NSEW)
root_button.grid(row=1, column=2, sticky=NSEW)
change_sign_button.grid(row=1, column=0, sticky=NSEW)

#button_actions
def clicked(button_name):
    if not isinstance(button_name, str):
        button_name = button_name.char
    if button_name == "clear":
        calc.second_number_turn == False
        calc.history.clear()
        output.set("0")
    elif button_name == "delete":
        if output.get() != "":
            output.set(output.get()[:-1])
    elif button_name == "decimal":
        calc.decimal_pressed = True
        output.set(output.get() + ".")
    elif button_name == "equal":
        try:
            calc.n2 = float(output.get())
            result = operations[calc.operator](calc.n1, calc.n2)
            output.set(str(result))
            calc.history.append(result)
        except ValueError:
            messagebox.showerror('error', 'not a valid number')
    elif button_name == "change sign":
        result = float(output.get()) * -1
        calc.history.append(result)
        output.set(str(result))
    elif button_name == "division":
        try:
            calc.n1 = float(output.get())
            calc.second_number_turn = True
            calc.operator = button_name
            output.set("")
        except ValueError:
            messagebox.showerror('error', 'not a valid number')
    elif button_name == "multiplication":
        try:
            calc.n1 = float(output.get())
            calc.second_number_turn = True
            calc.operator = button_name
            output.set("")
        except ValueError:
            messagebox.showerror('error', 'not a valid number')
    elif button_name == "addition":
        try:
            calc.n1 = float(output.get())
            calc.second_number_turn = True
            calc.operator = button_name
            output.set("")
        except ValueError:
            messagebox.showerror('error', 'not a valid number')
    elif button_name == "subtraction":
        try:
            calc.n1 = float(output.get())
            calc.second_number_turn = True
            calc.operator = button_name
            output.set("")
        except ValueError:
            messagebox.showerror('error', 'not a valid number')
    elif button_name == "exponent":
        try:
            calc.n1 = float(output.get())
            calc.second_number_turn = True
            calc.operator = button_name
            output.set("")
        except ValueError:
            messagebox.showerror('error', 'not a valid number')
    elif button_name == "root":
        try:
            calc.n1 = float(output.get())
            calc.second_number_turn = True
            calc.operator = button_name
            output.set("")
        except ValueError:
            messagebox.showerror('error', 'not a valid number')
    else:
        if output.get() == "0":
            output.set(button_name)
        else:
            output.set(output.get() + button_name)

#Key bindings
window.bind("<Return>", lambda event:clicked("equal"))
for i in range(10):
    window.bind(str(i), clicked)
window.bind("/", lambda event:clicked("division"))
window.bind("*", lambda event:clicked("multiplication"))
window.bind("+", lambda event:clicked("addition"))
window.bind("-", lambda event:clicked("subtraction"))
window.bind("^", lambda event:clicked("exponent"))
window.bind("r", lambda event:clicked("root"))
window.bind("n", lambda event:clicked("change sign"))
window.bind("c", lambda event:clicked("clear"))
window.bind(".", lambda event:clicked("decimal"))
window.bind("<BackSpace>", lambda event:clicked("delete"))
window.mainloop()
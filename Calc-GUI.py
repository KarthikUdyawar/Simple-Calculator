# import
from tkinter import *

#variable
expression = ""

# Functions
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""

    except:
        equation.set(" error ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

def delete():
    global expression
    expression = expression[:-1]
    equation.set(expression)


# Main function/gui
if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="black")
    gui.title("Simple Calculator")

    equation = StringVar()

    expression_field = Entry(gui, textvariable=equation, font=('calibre', 20, 'normal'), bg='lightgreen',  bd = 10)
    expression_field.grid(columnspan=4, pady=10)

    equation.set('Enter your expression')

    #Buttons
    clear = Button(gui, text='Clear', fg='white', bg='orange', font=('calibre', 10, 'bold'),
                   command=clear, height=2, width=8)
    clear.grid(row=1, column=0, padx=8, pady=8)

    delete = Button(gui, text='Delete', fg='white', bg='orange', font=('calibre', 10, 'bold'),
                    command=delete, height=2, width=8)
    delete.grid(row=1, column=1, padx=8, pady=8)

    divide = Button(gui, text=' / ', fg='white', bg='gray35', font=('calibre', 10, 'bold'),
                    command=lambda: press("/"), height=2, width=8)
    divide.grid(row=1, column=2, padx=8, pady=8)

    multiply = Button(gui, text=' * ', fg='white', bg='gray35', font=('calibre', 10, 'bold'),
                      command=lambda: press("*"), height=2, width=8)
    multiply.grid(row=1, column=3, padx=8, pady=8)

    button7 = Button(gui, text=' 7 ', fg='white', bg='grey', font=('calibre', 10, 'bold'),
                     command=lambda: press(7), height=2, width=8)
    button7.grid(row=2, column=0, padx=8, pady=8)

    button8 = Button(gui, text=' 8 ', fg='white', bg='grey', font=('calibre', 10, 'bold'),
                     command=lambda: press(8), height=2, width=8)
    button8.grid(row=2, column=1, padx=8, pady=8)

    button9 = Button(gui, text=' 9 ', fg='white', bg='grey', font=('calibre', 10, 'bold'),
                     command=lambda: press(9), height=2, width=8)
    button9.grid(row=2, column=2, padx=8, pady=8)

    minus = Button(gui, text=' - ', fg='white', bg='gray35', font=('calibre', 10, 'bold'),
                   command=lambda: press("-"), height=2, width=8)
    minus.grid(row=2, column=3, padx=8, pady=8)

    button4 = Button(gui, text=' 4 ', fg='white', bg='grey', font=('calibre', 10, 'bold'),
                     command=lambda: press(4), height=2, width=8)
    button4.grid(row=3, column=0, padx=8, pady=8)

    button5 = Button(gui, text=' 5 ', fg='white', bg='grey',  font=('calibre', 10, 'bold'),
                     command=lambda: press(5), height=2, width=8)
    button5.grid(row=3, column=1, padx=8, pady=8)

    button6 = Button(gui, text=' 6 ', fg='white', bg='grey', font=('calibre', 10, 'bold'),
                     command=lambda: press(6), height=2, width=8)
    button6.grid(row=3, column=2, padx=8, pady=8)

    plus = Button(gui, text=' + ', fg='white', bg='gray35', font=('calibre', 10, 'bold'),
                  command=lambda: press("+"), height=2, width=8)
    plus.grid(row=3, column=3, padx=8, pady=8)

    button1 = Button(gui, text=' 1 ', fg='white', bg='grey', font=('calibre', 10, 'bold'),
                     command=lambda: press(1), height=2, width=8)
    button1.grid(row=4, column=0, padx=8, pady=8)

    button2 = Button(gui, text=' 2 ', fg='white', bg='grey', font=('calibre', 10, 'bold'),
                     command=lambda: press(2), height=2, width=8)
    button2.grid(row=4, column=1, padx=8, pady=8)

    button3 = Button(gui, text=' 3 ', fg='white', bg='grey', font=('calibre', 10, 'bold'),
                     command=lambda: press(3), height=2, width=8)
    button3.grid(row=4, column=2, padx=8, pady=8)

    equal = Button(gui, text=' = ', fg='white', bg='orange', font=('calibre', 10, 'bold'),
                   command=equalpress, height=6, width=8)
    equal.grid(row=4, column=3, rowspan=2, padx=8, pady=8)

    button0 = Button(gui, text=' 0 ', fg='white', bg='grey', font=('calibre', 10, 'bold'),
                     command=lambda: press(0), height=2, width=20)
    button0.grid(row=5, column=0, columnspan=2, padx=8, pady=8)

    Decimal= Button(gui, text='.', fg='white', bg='grey', font=('calibre', 10, 'bold'),
                    command=lambda: press('.'), height=2, width=8)
    Decimal.grid(row=5, column=2, padx=8, pady=8)

    # start the GUI
    gui.mainloop()

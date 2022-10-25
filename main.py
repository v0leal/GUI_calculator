import tkinter as tk
import math
    # FUNCTIONS

def press_key(event):
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-*/':
        operation_button(event.char)
    elif event.char == '\r':
        calculate()
    else:
        entry.delete(-1,-1)

def add_digit(digit):
    value = entry.get()                     # Add digit to the entry row
    if value == 'Dividing by zero':
        entry.delete(0, 'end')                                  # If 'yes', delete the last operation symbol
        entry.insert('end', digit)
    else:
        entry.delete(0,'end')
        entry.insert('end', value + digit)                              # Insert digit
        if value[0] == '0' and len(value) == 1:                               # Check if the first digit '0'
            entry.delete(0, 1)                                  # If 'yes', delete the first '0', if not - pass

def add_digit_button(digit):                                # Add digit button
    return tk.Button(main, text=digit, bd=3,
                     command=lambda: add_digit(digit))

def add_operation_button(operation):                        # Add operation (+-*/) buttons
    return tk.Button(main, text=operation, bd=3,
                     command=lambda: operation_button(operation))

def operation_button(operation):                            # Insert operation to entry row
    value = entry.get()                                     # Save current entry row to a temporary variable
    if value == 'Dividing by zero':
        entry.delete(0, 'end')                                  # If 'yes', delete the last operation symbol
        entry.insert('end', '0')
    else:               # Delete current entry row
        if value[-1] in '+-/*' and len(value) == 1:                                 # Check if the last entry symbol is already operation mark
            value = value[:-1]
        elif '+' in value or '-' in value or '*' in value or '/' in value:
            calculate()
            value = entry.get()
        entry.delete(0, 'end')                                  # If 'yes', delete the last operation symbol
        entry.insert('end', value + str(operation))             # Add previous value of the entry row and add the new operation symbol

def add_clear_button():
    return tk.Button(main, text='C', bd=3,
                     command=lambda: clear_button())

def clear_button():
    entry.delete(0, 'end')
    entry.insert('end', '0')

def add_calculate_button():
    return tk.Button(main, text='=', bd=3,
                     command=lambda: calculate())
def calculate():
    try:
        if entry.get()[-1] in '+-*/':
            ans = entry.get() + entry.get()[:-1]
        else:
            ans = entry.get()
        entry.delete(0, 'end')
        if int(eval(ans)) == eval(ans):
            entry.insert('end', str(int(eval(ans))))
        else:
            entry.insert('end', str(eval(ans)))
    except ZeroDivisionError:
        ans = 'Dividing by zero'
        entry.delete(0, 'end')
        entry.insert('end', ans)

def delete_symb(event):
    value = entry.get()
    if len(value) == 1:
        entry.delete(0, 'end')
        entry.insert('end', '0')
    elif len(value[:-1]) > 0:
        entry.delete(0,'end')
        entry.insert('end', value[:-1])

    # INITIALISATION

        ## Main window

main = tk.Tk()                                               # Create main window
icon = tk.PhotoImage(file='icon.png')                        # Save icon of the main window
main.iconphoto(False, icon)                                  # Set icon of the main window
main.config(bg="#A6EBF2")                                    # Set default background color
main.title("L.V.'s GUI calculator")                          # Rename main window's title
main.geometry("300x400+200+250")                             # Set main window's default size (300px. x 400px.) and position (200px. from left border, 250px. from up border)
main.resizable(True, True)                                   # Property of resize-ability of main window
main.minsize(300, 400)                                       # Set minimum size of the main window
main.maxsize(500, 600)                                       # Set maximum size of the main window

main.bind('<Key>', press_key)
#main.bind('<Enter>', calculate)
main.bind('<BackSpace>', delete_symb)
    # WORKBENCH CUSTOMIZATION

        ## Rows
main.grid_rowconfigure(0, minsize=30)
main.grid_rowconfigure(1, minsize=30)
main.grid_rowconfigure(2, minsize=40)
main.grid_rowconfigure(3, minsize=40)
main.grid_rowconfigure(4, minsize=40)
main.grid_rowconfigure(5, minsize=40)

        ## Columns
main.grid_columnconfigure(0, minsize=50)
main.grid_columnconfigure(1, minsize=50)
main.grid_columnconfigure(2, minsize=50)
main.grid_columnconfigure(3, minsize=50)


    # ELEMENTS CREATING AND POSITION
        ## Label name
lable_name = tk.Label(main, text='L.V.\'s\nGUI calculator',  # Add text into 'main' window
                      bg='#999999',                          # Background color
                      fg='yellow',                           # Text color
                      width=15,                              # Set width of labelbox
                      height=2,                              # Set height of labelbox
                      font=('Times New Roman', 20, 'bold'),  # Set font, size, type
                      relief=tk.RAISED,                      # Create frame
                      bd=5                                   # Set frame's width
                      )
lable_name.grid(row=0, column=0, columnspan=3)               # Locate lable name

        ## Entry row
entry = tk.Entry(main, font=('Times New Roman', 20), justify=tk.RIGHT)  # Create entry row
entry.insert(0, '0')                                                    # Insert default value
entry.grid(row=1, column=0, columnspan=4, pady=20)                      # Locate entry row

        ## Digit buttons
btn1 = add_digit_button('1').grid(row=2, column=0, stick='ewns', padx=2, pady=2)
btn2 = add_digit_button('2').grid(row=2, column=1, stick='ewns', padx=2, pady=2)
btn3 = add_digit_button('3').grid(row=2, column=2, stick='ewns', padx=2, pady=2)
btn4 = add_digit_button('4').grid(row=3, column=0, stick='ewns', padx=2, pady=2)
btn5 = add_digit_button('5').grid(row=3, column=1, stick='ewns', padx=2, pady=2)
btn6 = add_digit_button('6').grid(row=3, column=2, stick='ewns', padx=2, pady=2)
btn7 = add_digit_button('7').grid(row=4, column=0, stick='ewns', padx=2, pady=2)
btn8 = add_digit_button('8').grid(row=4, column=1, stick='ewns', padx=2, pady=2)
btn9 = add_digit_button('9').grid(row=4, column=2, stick='ewns', padx=2, pady=2)
btn0 = add_digit_button('0').grid(row=5, column=1, stick='ewns', padx=2, pady=2)

        ## Operation buttons
btn_plus=add_operation_button('+').grid(row=2, column=3, stick='ewns', padx=2, pady=2)
bnt_minus=add_operation_button('-').grid(row=3, column=3, stick='ewns', padx=2, pady=2)
btn_multiply=add_operation_button('*').grid(row=4, column=3, stick='ewns', padx=2, pady=2)
btn=divide=add_operation_button('/').grid(row=5, column=3, stick='ewns', padx=2, pady=2)
btn_clr=add_clear_button().grid(row=5, column=0, stick='ewns', padx=2, pady=2)
btn_equals=add_calculate_button().grid(row=5, column=2, stick='ewns', padx=2, pady=2)

# CREATE MAIN WINDOW
main.mainloop()

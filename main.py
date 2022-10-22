import tkinter as tk
def add_digit(digit):
    entry.insert('end', digit)

#   Initialisation of main window
main = tk.Tk()                          # Create main window
icon = tk.PhotoImage(file='icon.png')   # Set icon of the main window
main.iconphoto(False, icon)             #
main.config(bg="#A6EBF2")               # Set default background color
main.title("L.V.'s GUI calculator")     # Rename main window's title
main.geometry("300x500")        # Set main window's default size (800px. x 500px.) and position (200px. from left border, 250px. from up border)
main.resizable(False, False)            # Property of resizeability of main window
#main.minsize(300, 400)                  # Set minimum size of the main window
#main.maxsize(500, 600)                  # Set maximum size of the main window

#   Name label
lable_name = tk.Label(main, text = 'L.V.\'s\nGUI calculator',       # Add text into 'main' window
                            bg = 'blue',                            # Background color
                            fg = 'yellow',                          # Text color
                            #width = 15,                             # Width of labelbox
                            #height = 2,                             # Height of labelbox
                            font = ('Times New Roman', 20, 'bold'), # Font, size, type
                            relief = tk.RAISED,                     # Frame
                            bd = 5                                  # Frame's width
                      ).grid(row=0, column=0, columnspan=3)

# Buttons
btn1 = tk.Button(main, text='1', bd=3, command= lambda: add_digit(1)).grid(row=2, column=0, stick='ewns', padx=2, pady=2)
btn2 = tk.Button(main, text='2', bd=3, command= lambda: add_digit(2)).grid(row=2, column=1, stick='ewns', padx=2, pady=2)
btn3 = tk.Button(main, text='3', bd=3, command= lambda: add_digit(3)).grid(row=2, column=2, stick='ewns', padx=2, pady=2)
btn4 = tk.Button(main, text='4', bd=3, command= lambda: add_digit(4)).grid(row=3, column=0, stick='ewns', padx=2, pady=2)
btn5 = tk.Button(main, text='5', bd=3, command= lambda: add_digit(5)).grid(row=3, column=1, stick='ewns', padx=2, pady=2)
btn6 = tk.Button(main, text='6', bd=3, command= lambda: add_digit(6)).grid(row=3, column=2, stick='ewns', padx=2, pady=2)
btn7 = tk.Button(main, text='7', bd=3, command= lambda: add_digit(7)).grid(row=4, column=0, stick='ewns', padx=2, pady=2)
btn8 = tk.Button(main, text='8', bd=3, command= lambda: add_digit(8)).grid(row=4, column=1, stick='ewns', padx=2, pady=2)
btn9 = tk.Button(main, text='9', bd=3, command= lambda: add_digit(9)).grid(row=4, column=2, stick='ewns', padx=2, pady=2)
btn0 = tk.Button(main, text='0', bd=3, command= lambda: add_digit(0)).grid(row=5, column=0, stick='ewns', padx=2, pady=2, columnspan=3)

# Entry
entry = tk.Entry(main, font=('Times New Roman', 20))
entry.grid(row=1, column=0, columnspan=3, pady=20)

main.grid_rowconfigure(1, minsize=30)
main.grid_rowconfigure(2, minsize=40)
main.grid_rowconfigure(3, minsize=40)
main.grid_rowconfigure(4, minsize=40)
main.grid_rowconfigure(5, minsize=40)
main.mainloop()

import tkinter as tk

#   Initialisation of main window
main = tk.Tk()                          # Create main window
icon = tk.PhotoImage(file='icon.png')   # Set icon of the main window
main.iconphoto(False, icon)             #
main.config(bg="#A6EBF2")               # Set default background color
main.title("L.V.'s GUI calculator")     # Rename main window's title
main.geometry("800x500+200+250")        # Set main window's default size (800px. x 500px.) and position (200px. from left border, 250px. from up border)
main.resizable(True, True)              # Property of resizeability of main window
main.minsize(300, 400)                  # Set minimum size of the main window
main.maxsize(500, 600)                  # Set maximum size of the main window


main.mainloop()

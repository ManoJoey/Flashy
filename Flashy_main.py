#Joey mocht je images willen gebruiken dan moet je command prompt opstarten en "pip install Pillow" zeggen, dan doet hij het
#Joey mocht je images willen gebruiken dan moet je command prompt opstarten en "pip install Pillow" zeggen, dan doet hij het
#Joey mocht je images willen gebruiken dan moet je command prompt opstarten en "pip install Pillow" zeggen, dan doet hij het
import tkinter as tk
from PIL import ImageTk,Image

homecount = 0

root = tk.Tk()
root.title("Flashy")
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
geometry = ("%dx%d" % (w,h))
root.geometry(geometry)

frame_home = tk.Frame(root)
frame_create = tk.Frame(root)

def clear_screen():
    #clears the screen
    frame_home.grid_forget()


def create_set():
    #creates a new study set
    clear_screen()
    frame_create.grid(row=0, column=0)


def home():
    #creates the home screen
    global homecount
    clear_screen()
    frame_home.grid(row=0, column=0)
    if homecount < 1:
        welcome_label = tk.Label(frame_home, text="Welcome!", font=("Helvetica", 50))
        welcome_label.grid(row=0, column=1, columnspan=3, pady=5)
        button_create = tk.Button(frame_home, text="Create new study set", width=18, height=5, borderwidth=5, font=("Helvetica", 20), command=create_set)
        button_create.grid(row=1, column=1)
        homecount += 1


#all the menu options
menu = tk.Menu(root)
root.config(menu=menu)
menu.add_command(label="Home", command=home)
menu.add_command(label="Create set", command=create_set)
menu.add_command(label="Exit", command=root.quit)


home()

root.grid_columnconfigure(0, weight=1)

root.mainloop()
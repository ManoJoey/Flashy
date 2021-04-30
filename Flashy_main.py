#Joey mocht je images willen gebruiken dan moet je command prompt opstarten en "pip install Pillow" zeggen, dan doet hij het
#Joey mocht je images willen gebruiken dan moet je command prompt opstarten en "pip install Pillow" zeggen, dan doet hij het
#Joey mocht je images willen gebruiken dan moet je command prompt opstarten en "pip install Pillow" zeggen, dan doet hij het
import tkinter as tk
from PIL import ImageTk,Image

homecount = 0

root = tk.Tk()
root.title("Flashy")
root.geometry("300x300")

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
        welcome_label = tk.Label(frame_home, text="Welcome!", font=("Helvetica", 25))
        welcome_label.pack(padx=70, pady=1)
        button_create = tk.Button(frame_home, text="Create new study set", width=20, height=3, command=create_set)
        button_create.pack()
        homecount += 1


#all the menu options
menu = tk.Menu(root)
root.config(menu=menu)
options_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="options", menu=options_menu)
options_menu.add_command(label="Home", command=home)
options_menu.add_command(label="Create set", command=create_set)
options_menu.add_command(label="Exit", command=root.quit)


home()

root.mainloop()
#Joey mocht je images willen gebruiken dan moet je command prompt opstarten en "pip install Pillow" zeggen, dan doet hij het
import tkinter as tk
from PIL import ImageTk,Image
from datetime import date

root = tk.Tk()
root.title("Flashy")
root.iconbitmap("F.ico")
root.wm_state('zoomed')
root.configure(background="black")


frame_home = tk.Frame(root, bg="black")
frame_create = tk.Frame(root, bg="black")
frame_study = tk.Frame(root, bg="black")


def clear_screen():
    #clears the screen
    frame_home.grid_forget()
    frame_create.grid_forget()
    frame_study.grid_forget()


def create_set():
    #creates a new study set
    clear_screen()
    frame_create.grid(row=0, column=0)


def study_set():
    #get button with changing title and definition
    clear_screen()
    frame_study.grid(row=0, column=0)


def home():
    #creates the home screen
    clear_screen()
    frame_home.grid(row=0, column=0)
    whitespace = tk.Label(frame_home, text="", bg="black", height=3)
    whitespace.grid(row=0, column=1)

    welcome_label = tk.Label(frame_home, text="Welcome!", font=("Helvetica", 50), fg="white", bg="black")
    welcome_label.grid(row=1, column=1, columnspan=3, pady=20)

    today = str(date.today().strftime("%d-%b-%Y"))
    today_date = tk.Label(frame_home, text=today, bg="black", fg="white", font=("Helvetica", 30))
    today_date.grid(row=2, column=1)

    whitespace.grid(row=3, column=1)

    button_create = tk.Button(frame_home, text="Create new study set", width=18, height=4, borderwidth=0, font=("Helvetica", 20), command=create_set)
    button_create.grid(row=4, column=1)

    start_studying = tk.Button(frame_home, text="Study a set", width=18, height=4, borderwidth=0, font=("Helvetica", 20), command=study_set)
    start_studying.grid(row=5, column=1, pady=2)

    exit_button = tk.Button(frame_home, text="Exit", width=26, height=3, borderwidth=0, font=("Helvetica", 15), command=root.quit)
    exit_button.grid(row=6, column=1, pady=100)


#all the menu options
menu = tk.Menu(root)
root.config(menu=menu)
menu.add_command(label="Home", command=home)
menu.add_command(label="Create set", command=create_set)
menu.add_command(label="Study set", command=study_set)
menu.add_command(label="Exit", command=root.quit)


home()

root.grid_columnconfigure(0, weight=1)

root.mainloop()
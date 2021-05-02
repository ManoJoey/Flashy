import tkinter as tk
from PIL import ImageTk,Image
from datetime import date
import pygame
import time

pygame.mixer.init()

homecount = 0

root = tk.Tk()
root.title("Flashy")
root.iconbitmap("F.ico")
root.wm_state('zoomed')
root.configure(background="black")


frame_home = tk.Frame(root, bg="black")
frame_create = tk.Frame(root, bg="black")
frame_study = tk.Frame(root, bg="black")
frame_image_side = tk.Frame(root, bg="black", width=750, height=996, borderwidth=0)
frame_image_side2 = tk.Frame(root, bg="black", width=750, height=996, borderwidth=0)

def quit_flashy():
    pygame.mixer.music.load("Minecraft hurt.mp3")
    pygame.mixer.music.play(loops=0)
    time.sleep(0.2)
    root.quit()

def clear_screen():
    #clears the screen
    frame_home.grid_forget()
    frame_create.grid_forget()
    frame_study.grid_forget()
    frame_image_side.grid_forget()
    frame_image_side2.grid_forget()


def done_creating():
    pass


def term_entered():
    term_entry.delete(0, tk.END)
    definition_entry.delete(0, tk.END)


def create_set():
    #creates a new study set
    global term_entry, definition_entry

    main_menu.entryconfig("Home", state="active")
    main_menu.entryconfig("Create set", state="disabled")
    main_menu.entryconfig("Study set", state="disabled")

    pygame.mixer.music.load("Mouse Click.mp3")
    pygame.mixer.music.play(loops=0)

    clear_screen()
    
    frame_create.grid(row=0, column=0)

    term_definition = tk.Label(frame_create, text="Term:                                   Definition:", bg="black", fg="#4c8151", font=("Helvetica", 30))
    term_definition.place(x=17, y=5)

    term_entry = tk.Entry(frame_create, width=75, borderwidth=0, bg="#4c8151")
    term_entry.grid(row=1, column=0, pady=70, padx=20)
    
    definition_entry = tk.Entry(frame_create, width=75, borderwidth=0, bg="#4c8151")
    definition_entry.grid(row=1, column=1, pady=70, padx=20)

    root.bind("<Return>", lambda event: term_entered())

    create_set_done = tk.Button(frame_create, text="Done", command=done_creating, width=10, height=2, bg="#4c8151", borderwidth=0)
    create_set_done.grid(row=2, column=1, sticky=tk.E)


def study_set():
    #get button with changing title and definition
    main_menu.entryconfig("Home", state="active")
    main_menu.entryconfig("Study set", state="disabled")
    main_menu.entryconfig("Create set", state="disabled")

    frame_image_side.grid_forget()
    frame_image_side2.grid_forget()

    pygame.mixer.music.load("Mouse Click.mp3")
    pygame.mixer.music.play(loops=0)

    clear_screen()
    frame_study.grid(row=0, column=0)


def home():
    #creates the home screen
    global homecount

    main_menu.entryconfig("Home", state="disabled")
    main_menu.entryconfig("Study set", state="active")
    main_menu.entryconfig("Create set", state="active")

    clear_screen()
    if homecount > 0:
        pygame.mixer.music.load("Mouse Click.mp3")
        pygame.mixer.music.play(loops=0)
    homecount += 1

    frame_image_side.grid(row=0, column=0)
    frame_home.grid(row=0, column=1)
    frame_image_side2.grid(row=0, column=2)

    whitespace = tk.Label(frame_home, text="", bg="black", height=3)
    whitespace.grid(row=0, column=1)

    welcome_label = tk.Label(frame_home, text="Welcome!", font=("Helvetica", 80), fg="#4c8151", bg="black")
    welcome_label.grid(row=1, column=1, columnspan=3, pady=20)

    today = str(date.today().strftime("%d-%b-%Y"))
    today_date = tk.Label(frame_home, text=today, bg="black", fg="#4c8151", font=("Helvetica", 50))
    today_date.grid(row=2, column=1, padx=35)

    whitespace.grid(row=3, column=1)

    button_create = tk.Button(frame_home, text="Create new study set", width=25, height=4, borderwidth=0, font=("Helvetica", 20), bg="#4c8151", command=create_set)
    button_create.grid(row=4, column=1, padx=8)

    start_studying = tk.Button(frame_home, text="Study a set", width=25, height=4, borderwidth=0, font=("Helvetica", 20), bg="#4c8151", command=study_set)
    start_studying.grid(row=5, column=1, pady=5, padx=8)

    exit_button = tk.Button(frame_home, text="Exit", width=25, height=3, borderwidth=0, font=("Helvetica", 20), bg="#4c8151", command=quit_flashy)
    exit_button.grid(row=6, column=1, pady=100)


#all the menu options
main_menu = tk.Menu(root)
root.config(menu=main_menu)
main_menu.add_command(label="Home", command=home)
main_menu.add_command(label="Create set", command=create_set)
main_menu.add_command(label="Study set", command=study_set)
main_menu.add_command(label="Exit", command=quit_flashy)


home()

big_f = tk.PhotoImage(file="F.png")
big_f_label = tk.Label(frame_image_side, image=big_f, bg="black")
big_f_label.grid(row=0, column=0)

big_f2 = tk.PhotoImage(file="Flashy full.png")
big_f_label2 = tk.Label(frame_image_side2, image=big_f2, bg="black")
big_f_label2.grid(row=0, column=0)


root.grid_columnconfigure(0, weight=1)

root.mainloop()
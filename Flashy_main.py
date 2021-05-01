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
frame_image_side = tk.Frame(root, bg="black", width=775, height=996, borderwidth=0)
frame_image_side2 = tk.Frame(root, bg="black", width=775, height=996, borderwidth=0)

def quit_flashy():
    pygame.mixer.music.load("Mouse Click.mp3")
    pygame.mixer.music.play(loops=0)
    time.sleep(0.15)
    root.quit()


def clear_screen():
    #clears the screen
    frame_home.grid_forget()
    frame_create.grid_forget()
    frame_study.grid_forget()


def create_set():
    #creates a new study set
    main_menu.entryconfig("Home", state="active")
    main_menu.entryconfig("Create set", state="disabled")
    main_menu.entryconfig("Study set", state="disabled")

    frame_image_side.grid_forget()
    frame_image_side2.grid_forget()

    pygame.mixer.music.load("Mouse Click.mp3")
    pygame.mixer.music.play(loops=0)

    clear_screen()
    frame_create.grid(row=0, column=0)


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

    frame_image_side.grid(row=0, column=0)
    frame_image_side2.grid(row=0, column=2)


    clear_screen()
    if homecount > 0:
        pygame.mixer.music.load("Mouse Click.mp3")
        pygame.mixer.music.play(loops=0)
    homecount += 1

    frame_home.grid(row=0, column=1)

    whitespace = tk.Label(frame_home, text="", bg="black", height=3)
    whitespace.grid(row=0, column=1)

    welcome_label = tk.Label(frame_home, text="Welcome!", font=("Helvetica", 50), fg="#4c8151", bg="black")
    welcome_label.grid(row=1, column=1, columnspan=3, pady=20)

    today = str(date.today().strftime("%d-%b-%Y"))
    today_date = tk.Label(frame_home, text=today, bg="black", fg="#4c8151", font=("Helvetica", 30))
    today_date.grid(row=2, column=1)

    whitespace.grid(row=3, column=1)

    button_create = tk.Button(frame_home, text="Create new study set", width=18, height=4, borderwidth=0, font=("Helvetica", 20), bg="#4c8151", command=create_set)
    button_create.grid(row=4, column=1)

    start_studying = tk.Button(frame_home, text="Study a set", width=18, height=4, borderwidth=0, font=("Helvetica", 20), bg="#4c8151", command=study_set)
    start_studying.grid(row=5, column=1, pady=5)

    exit_button = tk.Button(frame_home, text="Exit", width=26, height=3, borderwidth=0, font=("Helvetica", 15), bg="#4c8151", command=quit_flashy)
    exit_button.grid(row=6, column=1, pady=100)


#all the menu options
main_menu = tk.Menu(root)
root.config(menu=main_menu)
main_menu.add_command(label="Home", command=home)
main_menu.add_command(label="Create set", command=create_set)
main_menu.add_command(label="Study set", command=study_set)
main_menu.add_command(label="Exit", command=quit_flashy)


home()

frame_image_side.grid(row=0, column=0)
big_f = tk.PhotoImage(file="F.png")
big_f_label = tk.Label(frame_image_side, image=big_f, bg="black")
big_f_label.grid(row=0, column=0)
frame_image_side2.grid(row=0, column=2)
big_f_label2 = tk.Label(frame_image_side2, image=big_f, bg="black")
big_f_label2.grid(row=0, column=0)

root.mainloop()
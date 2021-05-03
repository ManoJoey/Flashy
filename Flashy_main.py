import tkinter as tk
from PIL import ImageTk,Image
from datetime import date
import pygame

pygame.mixer.init()

class Term:
    def __init__(self, term, definition):
        self.term = term
        self.definition = definition
    
    def fullstring(self):
        full_string = self.term + " | " + self.definition
        return full_string

    def split_line(self, line):
        x = line.split(" | ")
        self.term = x[0]
        self.definition = x[1]

def read_file(file_name):
    file_name_to_open = file_name + ".txt"
    file_ = open(file_name_to_open, "r")
    for item in file_:
        read_list.append(item)
    file_.close()

def writefile(file_name):
    file_write_to_open = file_name + ".txt"
    file_delete_to_open = file_name + ".txt"
    file_write = open(file_write_to_open, "a")
    file_delete = open(file_delete_to_open, "w")
    file_delete.write("")
    for item in write_list:
        item = str(item) + "\n"
        file_write.write(item)
    file_write.close()
    file_delete.close()

homecount = 0
y = 2
VisitCreateCount = 0
write_list = []
read_list = []
screenheightcount = 50
list_entries = []
list_entries_solid = []

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
    root.after(200, root.quit())

def clear_screen():
    #clears the screen
    frame_home.grid_forget()
    frame_create.grid_forget()
    frame_study.grid_forget()
    frame_image_side.grid_forget()
    frame_image_side2.grid_forget()


def done_creating():
    global write_list
    list_terms = []
    list_def = []
    term = True
    count = -1
    for entry in list_entries:
        if term:
            add_term = entry.get()
            list_terms.append(add_term)
            term = not term
        else:
            add_def = entry.get()
            list_def.append(add_def)
            term = not term
    for item in list_terms:
        count += 1
        t = Term
        set_v = Term(list_terms[count], list_def[count])
        line = t.fullstring(set_v)
        write_list.append(line)
    writefile("test")
    pygame.mixer.music.load("Party horn.mp3")
    pygame.mixer.music.play(loops=0)
    clear_screen()


def next_page():
    global screenheightcount
    clear_screen()
    for entry in list_entries:
        list_entries_solid.append(entry)
        if list_entries_solid.count(entry) == 2:
            list_entries_solid.pop(-1)
        entry.destroy()
    screenheightcount = 0

    next_page_term = tk.Entry(frame_create, width=75, borderwidth=0, bg="#4c8151")
    next_page_definition = tk.Entry(frame_create, width=75, borderwidth=0, bg="#4c8151")
    next_page_term.grid(row=1, column=0, padx=20)
    next_page_definition.grid(row=1, column=1, padx=85, pady=25)

    list_entries.append(next_page_term)
    list_entries.append(next_page_definition)

    frame_create.grid(row=0, column=0)

def add_term():
    global y, padcount, screenheightcount
    pygame.mixer.music.load("Swipe.mp3")
    pygame.mixer.music.play(loops=0)

    new_entry_term = tk.Entry(frame_create, width=75, borderwidth=0, bg="#4c8151")
    new_entry_term.grid(row=y, column=0, pady=25, padx=20)

    new_entry_definition = tk.Entry(frame_create, width=75, borderwidth=0, bg="#4c8151")
    new_entry_definition.grid(row=y, column=1, pady=25, padx=85)

    list_entries.append(new_entry_term)
    list_entries.append(new_entry_definition)

    create_set_done.grid_configure(row=y+2)
    new_term.grid_configure(row=y+2)

    y += 1
    screenheightcount += 78

    if screenheightcount > root.winfo_screenheight():
        next_page()


def create_set():
    #creates a new study set
    global term_entry, definition_entry, new_term, create_set_done, VisitCreateCount

    main_menu.entryconfig("Home", state="active")
    main_menu.entryconfig("Create set", state="disabled")
    main_menu.entryconfig("Study set", state="disabled")

    pygame.mixer.music.load("Mouse Click.mp3")
    pygame.mixer.music.play(loops=0)

    clear_screen()
    
    frame_create.grid(row=0, column=0)
    
    term_label = tk.Label(frame_create, text="Term:", bg="black", fg="#4c8151", font=("Helvetica", 20))
    term_label.grid(row=0, column=0, stick=tk.W, padx=20, pady=10)

    definition_label = tk.Label(frame_create, text="Definition:", bg="black", fg="#4c8151", font=("Helvetica", 20))
    definition_label.grid(row=0, column=1, stick=tk.W, padx=80, pady=10)

    term_entry = tk.Entry(frame_create, width=75, borderwidth=0, bg="#4c8151")
    term_entry.grid(row=1, column=0, padx=20)
    
    definition_entry = tk.Entry(frame_create, width=75, borderwidth=0, bg="#4c8151")
    definition_entry.grid(row=1, column=1, padx=85, pady=25)

    list_entries.append(term_entry)
    list_entries.append(definition_entry)

    new_term = tk.Button(frame_create, text="Add term", command=add_term, width=10, height=2, bg="#4c8151", borderwidth=0, font=("Helvetica", 15))
    new_term.grid(row=2, column=0, sticky=tk.W, padx=20, pady=25)
    root.bind("<Return>", lambda event: add_term())


    create_set_done = tk.Button(frame_create, text="Done", command=done_creating, width=10, height=2, bg="#4c8151", borderwidth=0, font=("Helvetica", 15))
    create_set_done.grid(row=2, column=1, sticky=tk.E, padx=88)

    VisitCreateCount += 1


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

    for entry in list_entries:
        list_entries_solid.append(entry)
        if list_entries_solid.count(entry) == 2:
            list_entries_solid.pop(-1)
        entry.destroy()
    
    if VisitCreateCount > 0:
        new_term.destroy()
        create_set_done.destroy()

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

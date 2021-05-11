import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
from datetime import date
import pygame
import os

pygame.mixer.init()
pygame.mixer.music.load("Pigstep.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.pause()

click = pygame.mixer.Sound("Mouse Click.mp3")

homecount = 0
y = 0
VisitCreateCount = 0
VisitStudyCount = 0
write_list = []
read_list = []
list_entries = []
list_entries_solid = []
title_set = ""
on = False

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
        if "\n" in item:
            read_list.append(item.replace("\n", ""))
        else:
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


root = tk.Tk()
root.geometry("-2000-0")
root.title("Flashy")
root.iconbitmap("F.ico")
root.state('zoomed')
root.configure(background="black")


frame_home = tk.Frame(root, bg="black")
frame_create = tk.Frame(root, bg="black")
frame_study = tk.Frame(root, bg="black")
frame_start_studying = tk.Frame(root, bg="black")
frame_view = tk.Frame(root, bg="black")
frame_image_side = tk.Frame(root, bg="black", width=750, height=996, borderwidth=0)
frame_image_side2 = tk.Frame(root, bg="black", width=750, height=996, borderwidth=0)
frame_image_create = tk.Frame(root, bg="black", width=750, height=996, borderwidth=0)
frame_done_creating = tk.Frame(root, bg="black")


def quit_flashy():
    pygame.mixer.music.load("Minecraft hurt.mp3")
    pygame.mixer.music.play(loops=0)
    root.after(200, root.quit())


def toggle_music():
    global on
    if on:
        pygame.mixer.music.pause()
        on = False
    elif on == False:
        pygame.mixer.music.unpause()
        on = True


def clear_screen():
    #clears the screen
    frame_home.grid_forget()
    frame_create.grid_forget()
    frame_study.grid_forget()
    frame_image_side.grid_forget()
    frame_image_side2.grid_forget()
    frame_image_create.grid_forget()
    frame_done_creating.grid_forget()
    frame_view.grid_forget()
    frame_start_studying.grid_forget()


def done_creating(title_set):
    if title_set != "Enter the title of your set here...":
        global write_list, list_entries, list_needed
        list_terms = []
        list_def = []
        term = True
        count = -1
        list_needed = list_entries
        for entry in list_needed:
            if term:
                if entry.get() != "":
                    add_term = entry.get()
                    list_terms.append(add_term)
                    term = not term
            else:
                if entry.get() != "":
                    add_def = entry.get()
                    list_def.append(add_def)
                    term = not term
        for item in list_terms:
            count += 1
            t = Term
            set_v = Term(list_terms[count], list_def[count])
            line = t.fullstring(set_v)
            write_list.append(line)
        title_set = title_entry.get()
        writefile(title_set)
        finish_sound = pygame.mixer.Sound("Party horn.mp3")
        finish_sound.play()
        clear_screen()
        list_entries = []
        list_needed = list_entries

        frame_done_creating.grid(row=0, column=0)
        label_done_creating = tk.Label(frame_done_creating, text="Your set has been saved!\nUse the menu to go back to the homepage.", fg="#4c8151", font=("Helvetica", 30), bg="black")
        label_done_creating.grid(row=0, column=0, pady=50)

        image_done_label.grid(row=1, column=0, pady=50)
    else:
        tk.messagebox.showerror("No title", "No title was entered.")


def add_term():
    global y, padcount, stringcount, create_canvas
    
    new_card_sound = pygame.mixer.Sound("Swipe.mp3")
    new_card_sound.play()

    entry_rank = tk.Label(second_frame, text=str(y+2), bg="black", fg="#4c8151")
    entry_rank.grid(row=y+1, column=0)

    new_entry_term = tk.Entry(second_frame, width=75, borderwidth=0, bg="#4c8151")
    new_entry_term.grid(row=y+1, column=1, pady=20, padx=20)

    new_entry_definition = tk.Entry(second_frame, width=75, borderwidth=0, bg="#4c8151")
    new_entry_definition.grid(row=y+1, column=2, pady=20, padx=85)

    list_entries.append(new_entry_term)
    list_entries.append(new_entry_definition)

    y += 1


def reset_scrollregion(self):
    create_canvas.configure(scrollregion=create_canvas.bbox("all"))


def on_mousewheel(event):
    #allows you to scroll
    create_canvas.yview_scroll(int(-1*(event.delta/120)), "units")


def title_clicked(clicked_entry):
    if clicked_entry.get() == "Enter the title of your set here...":
        clicked_entry.delete(0, tk.END)


def title_left(clicked_entry):
    if clicked_entry.get() == "":
        clicked_entry.delete(0, tk.END)
        clicked_entry.insert(0, "Enter the title of your set here...")
        root.focus()


def create_set():
    #creates a new study set
    global term_entry, definition_entry, new_term, create_set_done, VisitCreateCount, title_entry, y, second_frame, create_canvas
    y = 0

    click.play()

    main_menu.entryconfig("Home", state="active")
    main_menu.entryconfig("Study set", state="disabled")
    main_menu.entryconfig("Create set", state="disabled")
    main_menu.entryconfig("View sets", state="disabled")

    clear_screen()

    frame_create2 = tk.Frame(frame_create, bg="white")
    title_frame = tk.Frame(frame_create, bg="black")
    create_canvas = tk.Canvas(frame_create2, bg="black", width=1140, height=780, highlightthickness=5)
    second_frame = tk.Frame(create_canvas, bg="black")
    frame_buttons_create = tk.Frame(frame_create, bg="black")
    scrollbar = ttk.Scrollbar(frame_create2, orient=tk.VERTICAL, command=create_canvas.yview)

    frame_create.grid(row=1, column=0, sticky=tk.W)
    frame_create2.grid(row=1, column=0, sticky=tk.W)
    title_frame.grid(row=0, column=0, sticky=tk.W)

    create_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    create_canvas.configure(yscrollcommand=scrollbar.set)
    create_canvas.configure(scrollregion=create_canvas.bbox("all"))
    create_canvas.bind_all("<MouseWheel>", on_mousewheel)

    create_canvas.create_window((0,0), window=second_frame, anchor="nw")

    second_frame.bind("<Configure>", reset_scrollregion)

    frame_buttons_create.grid(row=2, column=0)

    title_label = tk.Label(title_frame, text="Title:", bg="black", fg="#4c8151", font=("Helvetica", 20))
    title_label.grid(row=0, column=0, sticky=tk.NW, padx=35)

    title_entry = tk.Entry(title_frame, width=62, borderwidth=0, bg="#4c8151")
    title_entry.grid(row=0, column=0, pady=12, padx=110)
    title_entry.insert(0, "Enter the title of your set here...")
    title_entry.bind("<Button-1>", lambda event: title_clicked(title_entry))
    title_entry.bind("<Enter>", lambda event: title_clicked(title_entry))
    title_entry.bind("<Leave>", lambda event: title_left(title_entry))

    term_label = tk.Label(title_frame, text="Term:", bg="black", fg="#4c8151", font=("Helvetica", 20))
    term_label.grid(row=1, column=0, stick=tk.W, padx=35, pady=10)

    definition_label = tk.Label(title_frame, text="Definition:", bg="black", fg="#4c8151", font=("Helvetica", 20))
    definition_label.grid(row=1, column=1, stick=tk.W, pady=10)

    new_term = tk.Button(frame_buttons_create, text="Add term", command=add_term, width=10, height=2, bg="#4c8151", borderwidth=0, font=("Helvetica", 15))
    new_term.grid(row=3, column=0, sticky="w", padx=20, pady=25)
    root.bind("<Return>", lambda event: add_term())

    create_set_done = tk.Button(frame_buttons_create, text="Done", command=lambda:done_creating(title_entry.get()), width=10, height=2, bg="#4c8151", borderwidth=0, font=("Helvetica", 15))
    create_set_done.grid(row=3, column=1, sticky="e", padx=850)

    frame_image_create.grid(row=1, column=0, sticky=tk.E)

    entry_rank1 = tk.Label(second_frame, text='1', bg="black", fg="#4c8151")
    entry_rank1.grid(row=y, column=0, padx=5)

    first_entry_term = tk.Entry(second_frame, width=75, borderwidth=0, bg="#4c8151")
    first_entry_term.grid(row=y, column=1, pady=20, padx=20)

    first_entry_definition = tk.Entry(second_frame, width=75, borderwidth=0, bg="#4c8151")
    first_entry_definition.grid(row=y, column=2, pady=20, padx=85)

    list_entries.append(first_entry_term)
    list_entries.append(first_entry_definition)

    VisitCreateCount += 1        


def show_def(event):
    #Still need to change text back but time and .after doesn't work
    click.play()
    for button in list_buttons_answers:
        if button is event.widget:
            index = list_terms.index(button["text"])
            button.config(text=list_answers[index])


def continue_with_file(button):
    global list_buttons_answers, list_terms, VisitStudyCount, list_answers
    list_buttons_answers = []
    list_terms = []
    list_answers = []
    xvar = 0
    yvar = 0

    click.play()

    text = button["text"]
    full_text = text + ".txt"
    opened_file = open(full_text, "r")

    clear_screen()
    frame_start_studying.grid(row=0, column=0)

    for line in opened_file.readlines():
        line = line.split(" | ")
        line[1] = line[1].rstrip("\n")

        button_term = tk.Button(frame_start_studying, text=line[0], width=20, height=2, bg="#4c8151", borderwidth=0, font=("Helvetica", 15))
        button_term.grid(row=yvar, column=xvar, padx=10, pady=10)
        button_term.bind("<Button-1>", show_def)
        list_buttons_answers.append(button_term)
        list_terms.append(line[0])
        list_answers.append(line[1])
        
        if (xvar - 6) < 0:
            xvar += 1
        else:
            xvar = xvar - 6
            yvar += 1

    VisitStudyCount += 1


def select_set(files):
    name_file = files.replace(".txt", "")
    button_select = tk.Button(frame_study, text=name_file, command=lambda: continue_with_file(button_select), width=20, height=2, bg="#4c8151", borderwidth=0, font=("Helvetica", 15))
    button_select.grid(row=they, column=thex, padx=10, pady=10)
    list_buttons_study.append(button_select)


def study_set():
    #you can select and study a set
    global thex, they, list_buttons_study
    list_buttons_study = []
    thex = 0
    they = 0
    main_menu.entryconfig("Home", state="active")
    main_menu.entryconfig("Study set", state="disabled")
    main_menu.entryconfig("Create set", state="disabled")
    main_menu.entryconfig("View sets", state="disabled")

    click.play()

    clear_screen()
    frame_study.grid(row=0, column=0)
    
    dirname = os.getcwd()

    ext = (".txt")
    for files in os.listdir(dirname):
        if files.endswith(ext):
            select_set(files)
                
            if (thex - 6) < 0:
                thex += 1
            else:
                thex = thex - 6
                they += 1


def view_sets():
    #allows you to view all the sets you have
    main_menu.entryconfig("Home", state="active")
    main_menu.entryconfig("Study set", state="disabled")
    main_menu.entryconfig("Create set", state="disabled")
    main_menu.entryconfig("View sets", state="disabled")

    click.play()

    clear_screen()
    frame_view.grid(row=0, column=0)


def home():
    #creates the home screen
    global homecount

    main_menu.entryconfig("Home", state="disabled")
    main_menu.entryconfig("Study set", state="active")
    main_menu.entryconfig("Create set", state="active")
    main_menu.entryconfig("View sets", state="active")

    clear_screen()

    if homecount > 0:
        click.play()
    homecount += 1

    for entry in list_entries:
        list_entries_solid.append(entry)
        if list_entries_solid.count(entry) == 2:
            list_entries_solid.pop(-1)
        entry.destroy()
    
    if VisitStudyCount > 0:
        for button in list_buttons_answers:
            button.destroy()

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

    view_sets_button = tk.Button(frame_home, text="View your sets", width=25, height=4, borderwidth=0, font=("Helvetica", 20), bg="#4c8151", command=view_sets)
    view_sets_button.grid(row=6, column=1)

    exit_button = tk.Button(frame_home, text="Exit", width=25, height=3, borderwidth=0, font=("Helvetica", 20), bg="#4c8151", command=quit_flashy)
    exit_button.grid(row=7, column=1, pady=70)


#all the menu options
main_menu = tk.Menu(root)
root.config(menu=main_menu)
main_menu.add_command(label="Home", command=home)
main_menu.add_command(label="Create set", command=create_set)
main_menu.add_command(label="Study set", command=study_set)
main_menu.add_command(label="View sets", command=view_sets)
main_menu.add_command(label="Toggle music", command=toggle_music)
main_menu.add_command(label="Exit", command=quit_flashy)


home()


ImageWidthVariable = 1980 / 700
round(ImageWidthVariable, 8)
WidthImage = root.winfo_screenwidth() / ImageWidthVariable

if root.winfo_screenwidth() > 1500:

    image1 = Image.open("F.png")
    image1 = image1.resize((int(WidthImage), 700), Image.ANTIALIAS)

    big_f = ImageTk.PhotoImage(image1)
    big_f_label = tk.Label(frame_image_side, image=big_f, bg="black")
    big_f_label.grid(row=0, column=0)


    image2 = Image.open("Flashy full.png")
    image2 = image2.resize((int(WidthImage), 700), Image.ANTIALIAS)

    big_f2 = ImageTk.PhotoImage(image2)
    big_f_label2 = tk.Label(frame_image_side2, image=big_f2, bg="black")
    big_f_label2.grid(row=0, column=0)


    image3 = Image.open("Flashy full.png")
    image3 = image3.resize((int(WidthImage), 700), Image.ANTIALIAS)

    big_f3 = ImageTk.PhotoImage(image3)
    big_f_label3 = tk.Label(frame_image_create, image=big_f3, bg="black")
    big_f_label3.grid(row=0, column=0)

image_done = Image.open("Check mark.png")
image_done = image_done.resize((500, 500), Image.ANTIALIAS)
image_done_full = ImageTk.PhotoImage(image_done)
image_done_label = tk.Label(frame_done_creating, image=image_done_full, bg="black")

root.grid_columnconfigure(0, weight=1)

root.mainloop()
#use grid.row/columnconfigure so that it will fit on all screens

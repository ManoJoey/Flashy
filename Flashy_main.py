import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
from datetime import date
import pygame
import os
import threading
import time

pygame.mixer.init()
pygame.mixer.music.load("Pigstep.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.pause()

click = pygame.mixer.Sound("Mouse Click.mp3")
finish_sound = pygame.mixer.Sound("Party horn.mp3")
new_card_sound = pygame.mixer.Sound("Swipe.mp3")

homecount = 0
y = 0
VisitStudy = False
VisitSet = False
VisitView = False
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
        file_delete.write(item)
    file_write.close()
    file_delete.close()


root = tk.Tk()
#root.geometry("-2000-0")
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
frame_image_create = tk.Frame(frame_create, bg="black", width=750, height=996, borderwidth=0)
frame_done_creating = tk.Frame(root, bg="black")
frame_view_set = tk.Frame(root, bg="black")
frame_done_view = tk.Frame(root, bg="black")


def quit_flashy():
    #if messagebox.askokcancel("Quit", "Do you want to quit?"):
        pygame.mixer.music.load("Minecraft hurt.mp3")
        pygame.mixer.music.play(loops=0)
        root.after(200, root.destroy())


def toggle_music():
    global on
    if on:
        pygame.mixer.music.pause()
        on = False
    elif on == False:
        pygame.mixer.music.unpause()
        on = True


def clear_screen():
    # clears the screen
    frame_home.grid_forget()
    frame_create.grid_forget()
    frame_study.grid_forget()
    frame_image_side.grid_forget()
    frame_image_side2.grid_forget()
    frame_image_create.grid_forget()
    frame_done_creating.grid_forget()
    frame_view.grid_forget()
    frame_start_studying.grid_forget()
    frame_done_view.grid_forget()
    if VisitSet:
        frame_start_studying2.pack_forget()
    if VisitView:
        frame_view_set.grid_forget()
        save_changes.grid_forget()
        add_item_b.grid_forget()

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
        finish_sound.play()
        clear_screen()
        list_entries = []
        list_needed = list_entries

        frame_done_creating.grid(row=0, column=0)
        label_done_creating = tk.Label(frame_done_creating, text="Your set has been saved!\nUse the menu to go back to the homepage.", fg="#4c8151", font=("Helvetica", 30), bg="black")
        label_done_creating.grid(row=0, column=0)

        image_done_label.grid(row=1, column=0, pady=100)
    else:
        tk.messagebox.showerror("No title", "No title was entered.")


def add_term():
    global y, padcount, create_canvas
    
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


def reset_scrollregion(self, canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))


def on_mousewheel(event, canvas):
    # allows you to scroll
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")


def title_clicked(clicked_entry):
    if clicked_entry.get() == "Enter the title of your set here...":
        clicked_entry.delete(0, tk.END)


def title_left(clicked_entry):
    if clicked_entry.get() == "":
        clicked_entry.delete(0, tk.END)
        clicked_entry.insert(0, "Enter the title of your set here...")
        root.focus()


def create_set():
    # creates a new study set
    global term_entry, definition_entry, new_term, create_set_done, title_entry, y, second_frame, create_canvas
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
    create_canvas.bind_all("<MouseWheel>", lambda event: on_mousewheel(event, create_canvas))

    create_canvas.create_window((0,0), window=second_frame, anchor="nw")

    second_frame.bind("<Configure>", lambda self: reset_scrollregion(self, create_canvas))

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
    new_term.grid(row=0, column=0, sticky="w", padx=20, pady=25)
    root.bind("<Return>", lambda event: add_term())

    create_set_done = tk.Button(frame_buttons_create, text="Done", command=lambda:done_creating(title_entry.get()), width=10, height=2, bg="#4c8151", borderwidth=0, font=("Helvetica", 15))
    create_set_done.grid(row=0, column=1, sticky="e", padx=850)
    root.bind("<+>", lambda event: done_creating(title_entry.get()))

    frame_image_create.grid(row=1, column=0, sticky=tk.E)

    entry_rank1 = tk.Label(second_frame, text='1', bg="black", fg="#4c8151")
    entry_rank1.grid(row=y, column=0, padx=5)

    first_entry_term = tk.Entry(second_frame, width=75, borderwidth=0, bg="#4c8151")
    first_entry_term.grid(row=y, column=1, pady=20, padx=20)

    first_entry_definition = tk.Entry(second_frame, width=75, borderwidth=0, bg="#4c8151")
    first_entry_definition.grid(row=y, column=2, pady=20, padx=85)

    list_entries.append(first_entry_term)
    list_entries.append(first_entry_definition)

    # give frames weight so resizes correctly
    title_frame.grid_columnconfigure(0, weight=1)
    title_frame.grid_columnconfigure(1, weight=1)
    title_frame.grid_rowconfigure(0, weight=1)
    title_frame.grid_rowconfigure(1, weight=1)


def timer_thread(name, item, button, requested_time, index):
    button.config(text=list_answers[index], bg="black", fg="#4c8151")
    time.sleep(requested_time)
    button.config(text=item, bg="#4c8151", fg="black")


def show_def(event):
    click.play()
    for button in list_buttons_answers:
        if button is event.widget:
            try:
                index = list_terms.index(button["text"])
                requested_time = int(time_wanted)
                x = threading.Thread(target=timer_thread, args=(1, list_terms[index], list_buttons_answers[index], requested_time, index), daemon=True)
                x.start()
            except:
                if tk.messagebox.askokcancel("Something went wrong", "Something went wrong.\n\nPerhaps you didn't fill in a time or clicked a button while it was displaying an answer?\n\nDo you want to go back to the main menu:"):
                    home()


def enter_time(window, entry):
    try:
        int(entry)
        window.destroy()
        global time_wanted
        time_wanted = entry
    except:
        tk.messagebox.showerror("Integer", "Please enter an integer")
        window.attributes("-topmost", 1)
        window.after_idle(window.attributes, '-topmost', 0)


def toplevel():
    top = tk.Toplevel()
    top.geometry("420x120")
    top.title("Time")
    top.iconbitmap("F.ico")
    top.config(bg="black")
    top.attributes("-topmost", 1)
    top.grab_set()

    WindowWidth = top.winfo_reqwidth()
    WindowHeight = top.winfo_reqheight()

    positionRight = int(root.winfo_screenwidth()/2 - WindowWidth/2)
    positionDown = int(root.winfo_screenheight()/2 - WindowHeight/2)
    top.geometry("+{}+{}".format(positionRight, positionDown))

    top_label = tk.Label(top, text="How long do you want to see the answer for?", bg="black", fg="#4c8151", font=("Helvetica", 15))
    top_label.pack(pady=10)

    top_entry = tk.Entry(top, bg="#4c8151", fg="black", bd=0, width=30)
    top_entry.pack()

    done_b_top = tk.Button(top, text="Enter", bg="black", fg="#4c8151", bd=0, font=("Helvetica", 15), command=lambda: enter_time(top, top_entry.get()))
    done_b_top.pack(pady=10)
    top.bind("<Return>", lambda event: enter_time(top, top_entry.get()))


def continue_with_file(button):
    global list_buttons_answers, list_terms, VisitStudy, list_answers, frame_start_studying2, VisitSet

    root.rowconfigure(0, weight=1)

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
    frame_start_studying.grid(row=0, column=0, sticky=tk.NSEW)
    
    frame_start_studying2 = tk.Frame(frame_start_studying, bg="black")
    frame_start_studying2.pack(fill=tk.BOTH, expand=1)
    
    study_canvas = tk.Canvas(frame_start_studying2, bg="black")
    study_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    study_canvas.bind_all("<MouseWheel>", lambda event: on_mousewheel(event, study_canvas))

    study_scrollbar = ttk.Scrollbar(frame_start_studying2, orient=tk.VERTICAL, command=study_canvas.yview)
    study_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    study_canvas.configure(yscrollcommand=study_scrollbar.set)
    study_canvas.bind("<Configure>", lambda event: study_canvas.configure(scrollregion=study_canvas.bbox("all")))

    study_canvas_frame = tk.Frame(study_canvas, bg="black")

    study_canvas.create_window((0, 0), window=study_canvas_frame, anchor="nw")

    study_canvas_frame.bind("<Configure>", lambda self: reset_scrollregion(self, study_canvas))

    VisitSet = True

    WidthVar = 22 / 1920
    HeightVar = 2 / 997
    width = int(root.winfo_width()) * WidthVar
    width = int(round(width))
    height = int(root.winfo_height()) * HeightVar
    height = int(round(height))

    PadVar = 10 / 1920
    distance = int(root.winfo_width()) * PadVar
    distance = int(round(distance))

    for line in opened_file.readlines():
        line = line.split(" | ")
        line[1] = line[1].rstrip("\n")
        button_term = tk.Button(study_canvas_frame, text=line[0], width=width, height=height, bg="#4c8151", borderwidth=0, font=("Helvetica", 15))
        button_term.grid(row=yvar, column=xvar, padx=distance, pady=distance)
        button_term.bind("<Button-1>", show_def)
        list_buttons_answers.append(button_term)
        list_terms.append(line[0])
        list_answers.append(line[1])
        
        if (xvar - 6) < 0:
            xvar += 1
        else:
            xvar = xvar - 6
            yvar += 1

    toplevel()

    VisitStudy = True

    # give study_canvas_frame weight
    columns = int(study_canvas_frame.grid_size()[0])
    rows = int(study_canvas_frame.grid_size()[1])
    for c in range(columns):
        study_canvas_frame.grid_columnconfigure(c, weight=1)
    for r in range(rows):
        study_canvas_frame.grid_rowconfigure(r, weight=1)


def select_set(files):
    name_file = files.replace(".txt", "")
    button_select = tk.Button(frame_study, text=name_file, command=lambda: continue_with_file(button_select), width=20, height=2, bg="#4c8151", borderwidth=0, font=("Helvetica", 15))
    button_select.grid(row=they, column=thex, padx=10, pady=10)
    list_buttons_study.append(button_select)


def study_set():
    # you can select and study a set
    global thex, they, list_buttons_study

    root.columnconfigure(0, weight=1)
    root.columnconfigure(2, weight=0)
    root.rowconfigure(0, weight=0)

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


def view_entry(term, definition):
    global y, padcount, create_canvas

    entry_rank = tk.Label(view_canvas_frame, text=str(y+1), bg="black", fg="#4c8151")
    entry_rank.grid(row=y+1, column=0)

    new_entry_term = tk.Entry(view_canvas_frame, width=75, borderwidth=0, bg="#4c8151")
    new_entry_term.grid(row=y+1, column=1, pady=20, padx=20)
    new_entry_term.insert(0, term)

    new_entry_definition = tk.Entry(view_canvas_frame, width=75, borderwidth=0, bg="#4c8151")
    new_entry_definition.grid(row=y+1, column=2, pady=20, padx=85)
    new_entry_definition.insert(0, definition)

    list_entries_view.append(new_entry_term)
    list_entries_view.append(new_entry_definition)

    y += 1


def save_edited_set(opened_file):
    t = []
    d = []
    is_term = True
    count = 0
    
    for item in list_entries_view:
        if is_term:
            t.append(item.get())   
        elif is_term == False:
            d.append(item.get())
        is_term = not is_term
    for item in t:
        item_to_add = item + " | " + d[count]
        write_list.append(item_to_add)
        count += 1
    opened_file = opened_file.strip(".txt")
    writefile(opened_file)

    clear_screen()
    finish_sound.play()

    frame_done_view.grid(row=0, column=0)
    label_done_view = tk.Label(frame_done_view, text="Your changes have been saved!\nUse the menu to go back to the homepage.", fg="#4c8151", font=("Helvetica", 30), bg="black")
    label_done_view.grid(row=0, column=0)
    image_done_label2.grid(row=1, column=0, pady=100)


def add_item():
    new_card_sound.play()
    row = int(view_canvas_frame.grid_size()[1])

    rank = tk.Label(view_canvas_frame, text=str(row), bg="black", fg="#4c8151")
    rank.grid(row=row, column=0)

    new_entry0 = tk.Entry(view_canvas_frame, width=75, borderwidth=0, bg="#4c8151")
    new_entry0.grid(row=row, column=1, pady=20, padx=20)
    list_entries_view.append(new_entry0)

    new_entry1 = tk.Entry(view_canvas_frame, width=75, borderwidth=0, bg="#4c8151")
    new_entry1.grid(row=row, column=2, pady=20, padx=85)
    list_entries_view.append(new_entry1)


def view_selected_file(selected_button):
    global list_entries_view, view_canvas_frame, VisitView, y, save_changes, add_item_b

    columns = int(root.grid_size()[0])
    rows = int(root.grid_size()[1])
    for c in range(columns):
        root.grid_columnconfigure(c, weight=0)
    for r in range(rows):
        root.grid_rowconfigure(r, weight=0)
    
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    click.play()
    
    list_entries_view = []
    text = selected_button["text"]
    text1 = str(text + ".txt")
    current_file = open(text1, "r")

    WidthVar = 22 / 1920
    HeightVar = 2 / 997
    width = int(root.winfo_width()) * WidthVar
    width = int(round(width))
    height = int(root.winfo_height()) * HeightVar
    height = int(round(height))

    PadVar = 10 / 1920
    distance = int(root.winfo_width()) * PadVar
    distance = int(round(distance))
    
    clear_screen()
    frame_view_set.grid(row=0, column=0, sticky=tk.NSEW)

    frame_view_set1 = tk.Frame(frame_view_set, bg="black")
    frame_view_set1.pack(fill=tk.BOTH, expand=1)

    view_canvas = tk.Canvas(frame_view_set1, bg="black")
    view_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    view_canvas.bind_all("<MouseWheel>", lambda event: on_mousewheel(event, view_canvas))

    view_scrollbar = ttk.Scrollbar(frame_view_set1, orient=tk.VERTICAL, command=view_canvas.yview)
    view_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    view_canvas.configure(yscrollcommand=view_scrollbar.set)
    view_canvas.bind("<Configure>", lambda event: view_canvas.configure(scrollregion=view_canvas.bbox("all")))

    view_canvas_frame = tk.Frame(view_canvas, bg="black")

    view_canvas.create_window((0, 0), window=view_canvas_frame, anchor="nw")

    view_canvas_frame.bind("<Configure>", lambda self: reset_scrollregion(self, view_canvas))

    save_changes = tk.Button(root, text="Save changes", command=lambda: save_edited_set(text), width=15, height=2, bg="#4c8151", borderwidth=0, font=("Helvetica", 15))
    save_changes.grid(row=1, column=0, sticky=tk.W, pady=20, padx=30)

    add_item_b = tk.Button(root, text="Add term", command=add_item, width=15, height=2, bg="#4c8151", borderwidth=0, font=("Helvetica", 15))
    add_item_b.grid(row=1, column=0, sticky=tk.E, pady=20, padx=30)
    root.bind("<Return>", lambda event: add_item())


    for line in current_file:
        line = line.split(" | ")
        line[1] = line[1].rstrip("\n")
        
        view_entry(line[0], line[1])
    
    y = 0
    
    VisitView = True


def view_all_sets(selected_file):
    list_buttons_view = []
    name_file = selected_file.replace(".txt", "")
    button_view = tk.Button(frame_view, text=name_file, command=lambda: view_selected_file(button_view), width=20, height=2, bg="#4c8151", borderwidth=0, font=("Helvetica", 15))
    button_view.grid(row=Yview, column=Xview, padx=10, pady=10)
    list_buttons_view.append(button_view)


def view_sets():
    # allows you to view all the sets you have
    global Xview, Yview

    root.columnconfigure(0, weight=1)
    root.columnconfigure(2, weight=0)
    root.rowconfigure(0, weight=0)

    main_menu.entryconfig("Home", state="active")
    main_menu.entryconfig("Study set", state="disabled")
    main_menu.entryconfig("Create set", state="disabled")
    main_menu.entryconfig("View sets", state="disabled")

    Xview = 0
    Yview = 0

    click.play()

    clear_screen()
    frame_view.grid(row=0, column=0)
    
    dirname = os.getcwd()

    ext = (".txt")
    for files in os.listdir(dirname):
        if files.endswith(ext):
            view_all_sets(files)

            if (Xview - 6) < 0:
                Xview += 1
            else:
                Xview = Xview - 6
                Yview += 1


def home():
    # creates the home screen
    global homecount

    root.columnconfigure(0, weight=1)
    root.columnconfigure(2, weight=0)
    root.rowconfigure(0, weight=1)

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
    
    if VisitStudy:
        for button in list_buttons_answers:
            button.destroy()
    
    if VisitView:
        for child in frame_view_set.winfo_children():
            child.destroy()

    frame_image_side.grid(row=0, column=0, sticky="nsew")
    frame_home.grid(row=0, column=1, sticky="nsew")
    frame_image_side2.grid(row=0, column=2, sticky="nsew")

    whitespace = tk.Label(frame_home, text="", bg="black", height=3)
    whitespace.grid(row=0, column=0, sticky="nsew")

    welcome_label = tk.Label(frame_home, text="Welcome!", font=("Helvetica", 80), fg="#4c8151", bg="black")
    welcome_label.grid(row=1, column=0, columnspan=3, pady=20, sticky="nsew")

    today = str(date.today().strftime("%d-%b-%Y"))
    today_date = tk.Label(frame_home, text=today, bg="black", fg="#4c8151", font=("Helvetica", 50))
    today_date.grid(row=2, column=0, padx=35, sticky="nsew")

    whitespace.grid(row=3, column=0)

    button_create = tk.Button(frame_home, text="Create new study set", width=25, height=4, borderwidth=0, font=("Helvetica", 20), bg="#4c8151", command=create_set)
    button_create.grid(row=4, column=0, padx=8, sticky="nsew")

    start_studying = tk.Button(frame_home, text="Study a set", width=25, height=4, borderwidth=0, font=("Helvetica", 20), bg="#4c8151", command=study_set)
    start_studying.grid(row=5, column=0, pady=5, padx=8, sticky="nsew")

    view_sets_button = tk.Button(frame_home, text="View your sets", width=25, height=4, borderwidth=0, font=("Helvetica", 20), bg="#4c8151", command=view_sets)
    view_sets_button.grid(row=6, column=0, sticky="nsew")

    exit_button = tk.Button(frame_home, text="Exit", width=25, height=3, borderwidth=0, font=("Helvetica", 20), bg="#4c8151", command=quit_flashy)
    exit_button.grid(row=7, column=0, pady=70, sticky="nsew")


# all the menu options
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
image_done_label2 = tk.Label(frame_done_view, image=image_done_full, bg="black")

def WeighItDown():
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    # frame home
    frame_home.grid_columnconfigure(0, weight=1)
    frame_home.grid_columnconfigure(1, weight=1)
    frame_home.grid_rowconfigure(0, weight=1)
    frame_home.grid_rowconfigure(1, weight=1)
    frame_home.grid_rowconfigure(2, weight=1)
    frame_home.grid_rowconfigure(3, weight=1)
    frame_home.grid_rowconfigure(4, weight=1)
    frame_home.grid_rowconfigure(5, weight=1)
    frame_home.grid_rowconfigure(6, weight=1)
    frame_home.grid_rowconfigure(7, weight=1)

    # frame create
    frame_create.grid_columnconfigure(0, weight=1)
    frame_create.grid_columnconfigure(0, weight=1)
    frame_create.grid_rowconfigure(0, weight=1)
    frame_create.grid_rowconfigure(1, weight=0)
    frame_create.grid_rowconfigure(2, weight=1)

    # frame study
    frame_study.grid_columnconfigure(0, weight=1)
    frame_study.grid_columnconfigure(1, weight=1)
    frame_study.grid_columnconfigure(2, weight=1)
    frame_study.grid_columnconfigure(3, weight=1)
    frame_study.grid_columnconfigure(4, weight=1)
    frame_study.grid_columnconfigure(5, weight=1)
    frame_study.grid_columnconfigure(6, weight=1)
    frame_study.grid_rowconfigure(0, weight=1)
    frame_study.grid_rowconfigure(1, weight=1)
    frame_study.grid_rowconfigure(2, weight=1)
    frame_study.grid_rowconfigure(3, weight=1)

    # frame view
    frame_view.grid_columnconfigure(0, weight=1)
    frame_view.grid_columnconfigure(1, weight=1)
    frame_view.grid_columnconfigure(2, weight=1)
    frame_view.grid_columnconfigure(3, weight=1)
    frame_view.grid_columnconfigure(4, weight=1)
    frame_view.grid_columnconfigure(5, weight=1)
    frame_view.grid_columnconfigure(6, weight=1)
    frame_view.grid_rowconfigure(0, weight=1)
    frame_view.grid_rowconfigure(1, weight=1)
    frame_view.grid_rowconfigure(2, weight=1)
    frame_view.grid_rowconfigure(3, weight=1)

    # frame done creating
    frame_done_creating.grid_rowconfigure(0, weight=1)
    frame_done_creating.grid_rowconfigure(1, weight=1)
    frame_done_creating.grid_columnconfigure(0, weight=1)

WeighItDown()

root.protocol("WM_DELETE_WINDOW", quit_flashy)

root.mainloop()
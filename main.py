
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import os

from doctor import *
from patient import *
from appointment import *

import database
database.init_db()

from PIL import ImageTk, Image

#database.reset_tables()   # reset table for test

# to use Tk function as window
window = Tk()     
# window title
window.title("Hospital Management System (HMS)")
window.geometry("390x220")
window.resizable(width = "False", height = "False")
Label(window, text = "Patient Registration System ", font = "Verdana 14 bold", fg = "black", bg = "#007bff", bd = "5px").pack()

# adding image
image_path = os.path.join("images","pngtree-user-login-or-authenticate-icon-on-gray-background-flat-icon-ve-png-image_5089976.jpg")
original_img = Image.open(image_path)
resized_image = original_img.resize((100,100))
img = ImageTk.PhotoImage(resized_image)
label_img = Label(window, image = img)
label_img.place(x=260,y=75)


L3 = Label(window)
L3.place(x=148, y= 200)

# login page function

def login():
    # we will control the E1 and E2 with get() to login successfully or not
    if (E1.get() == str("admin")) and (E2.get() == str("")):
        messagebox.showinfo("Successful login", "Logged in successfully.")
        window.destroy()
        open_main_screen()   
    else:
        messagebox.showerror("Error", "Incorrect login")
        
  
# sidebar of the main page

def create_sidebar(parent):
    sidebar = tk.Frame(parent, bg="#007bff", width =250)
    sidebar.pack(side = tk.LEFT, fill = tk.Y)  
    
    
     # admin image
    
    original_admin_image = Image.open("images\images.jpeg")
    resized_admin_image = original_admin_image.resize((200,200)) 
    img2 = ImageTk.PhotoImage(resized_admin_image)
    label_img2 = Label(sidebar, image = img2)
    label_img2.image = img2  
    label_img2.pack(pady = 10, padx = 10, side=tk.TOP)
   
    # welcome label
    
    welcome_label = Label(sidebar, text="Welcome,\n\n Admin",  bg="#007bff", fg="black", font=('Arial', 14))
    welcome_label.pack(pady=(0, 20), padx=10, side=tk.TOP) 
    
    # menu buttons
    buttons = [
        ("Dashboard",lambda: print("Dashboard clicked")),
        ("Doctor", lambda: open_doctor_page(parent)),
        ("Patient",lambda: open_patient_page(parent)),
        ("Appointment", lambda: open_appointment_page(parent))
    ]
    
    for button_text,command in buttons:
        btn = tk.Button(sidebar, text = button_text, bg='#007bff', fg='white', font=('Arial', 15), relief=tk.FLAT, cursor ="hand2", command=command)
        btn.pack(fill= tk.X, pady=10)
        
    
    return sidebar     

# main page cards

def create_cards(parent):
     stats_frame = tk.Frame(parent)
     stats_frame.pack(pady=20)
     
     # info of the cards
     # dynamic information with database 
     card_info = [
        {'label': 'Total Doctor', 'value': database.get_total_doctors(), 'color': '#343a40'},
        {'label': 'Total Patient', 'value': database.get_total_patients(), 'color': '#ff8000'},
        {'label': 'Total Appointment', 'value': database.get_total_appointments(), 'color': '#007bff'},
    ]
     
     for info in card_info:
        card = tk.Frame(stats_frame, bg=info['color'], width=200, height=100)
        card.pack(side=tk.LEFT, padx=10)

        label_value = tk.Label(card, text=info['value'], fg='white', bg=info['color'], font=('Arial', 24))
        label_value.pack(pady=10)  
            
        label_text = tk.Label(card, text=info['label'], fg='white', bg=info['color'], font=('Arial', 12))
        label_text.pack(pady=5)
         
     return stats_frame
 
# table part of the main page

def create_table(parent, title, columns,data):
    table_frame = tk.Frame(parent)
    table_frame.pack(pady=10)
    
    title_label = tk.Label(table_frame, text=title, font=('Arial',14))
    title_label.pack()
    
    style = ttk.Style()
    style.configure("Treeview.Heading", font=('Arial', 12, 'bold'), foreground="blue")
    
    
    # ttk module for create tables with columns and rows
    tree = ttk.Treeview(table_frame, columns = columns, show = 'headings', height =5)
    
    # column headings
    for col in columns:
        tree.heading(col, text =col, anchor = tk.CENTER)
        tree.column(col, width=150, anchor = tk.CENTER)
        
    # add data to the table
    for row in data:
        tree.insert('',tk.END, values = row)
        
    
    tree.pack()

# table columns
recent_doctors_columns = ['Name', 'Department', 'Contact', 'Status']
recent_patients_columns = ['Name', 'Symptoms', 'Contact', 'Address', 'Status']


# table for appointments

def create_appointments_table(parent):
    appointments = database.get_all_appointments()
    appointment_columns = ['Doctor','Patient', 'Date']
    create_table(parent, "Appointments", appointment_columns,appointments)


# open main screen function with properties

def open_main_screen():
    main_screen = tk.Tk()
    main_screen.title("Main Screen")
    main_screen.geometry("1000x600")
    
    
    create_sidebar(main_screen)
    create_cards(main_screen)

    recent_doctors = database.get_recent_doctors()
    recent_patients = database.get_recent_patients()
    
    
    recent_doctors_columns = ['Name', 'Department', 'Contact', 'Status']
    create_table(main_screen,"Recent Doctors", recent_doctors_columns, recent_doctors )
    
    recent_patients_columns = ['Name', 'Symptoms', 'Contact', 'Address', 'Status']
    create_table(main_screen, "Recent Patients", recent_patients_columns, recent_patients)
    
    new_patient_id = 1
    assignment_result = assign_doctor_to_patient(new_patient_id)
    print(assignment_result)
    
    create_appointments_table(main_screen)
    
    
    main_screen.mainloop()
  

# user login page

L1 = Label(window, text = "Username" )
L1.place(x=75, y=55)
E1 = Entry(window, width= 25 )
E1.place(x=77, y=85)
L2 = Label(window, text = "Password" )
L2.place(x=75, y=120)
E2 = Entry(window, width= 25 )
E2.place(x=77, y=150)

btn = Button(window,
             text =  "Login",
             padx = "20", pady = "5",fg = "black", bg = "#007bff" ,
             command= login)
        
btn.place(x=120,y=180)

window.mainloop()     # to show program
from tkinter import *
from tkinter import messagebox
import database

# doctor screen

def open_doctor_page(main_screen):
    doctor_window =Toplevel(main_screen)
    doctor_window.title("Add Doctor")
    doctor_window.geometry("300x300")
    
    Label(doctor_window, text="Name:").pack(pady=5)
    doctor_name_entry = Entry(doctor_window)
    doctor_name_entry.pack(pady=5)
    
    Label(doctor_window, text="Department:").pack(pady=5)
    department_entry = Entry(doctor_window)
    department_entry.pack(pady=5)

    Label(doctor_window, text="Contact:").pack(pady=5)
    contact_entry = Entry(doctor_window)
    contact_entry.pack(pady=5)
    
    def add_doctor():
        name = doctor_name_entry.get()
        department = department_entry.get()
        contact = contact_entry.get()
        
        database.add_doctor(name,department,contact) # add to database
    
        messagebox.showinfo("Success", "Doctor added successfully.")
        doctor_window.destroy()
        
    Button(doctor_window, text="Add Doctor", command=add_doctor).pack(pady=20)
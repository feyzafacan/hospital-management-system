from tkinter import *
from tkinter import messagebox
import database

# patient screen

def open_patient_page(main_screen):
    patient_window =Toplevel(main_screen)
    patient_window.title("Add Patient")
    patient_window.geometry("300x300")
    
    Label(patient_window, text="Name:").pack(pady=5)
    patient_name_entry = Entry(patient_window)
    patient_name_entry.pack(pady=5)
    
    Label(patient_window, text="Symptoms:").pack(pady=5)
    symptoms_entry = Entry(patient_window)
    symptoms_entry.pack(pady=5)

    Label(patient_window, text="Contact:").pack(pady=5)
    contact_entry = Entry(patient_window)
    contact_entry.pack(pady=5)
    
    Label(patient_window, text="Address:").pack(pady=5)
    address_entry = Entry(patient_window)
    address_entry.pack(pady=5)
    
    def add_patient():
        name = patient_name_entry.get()
        symptoms = symptoms_entry.get()
        contact = contact_entry.get()
        address = address_entry.get()
        
        database.add_patient(name,symptoms,contact,address) # add to database
    
        messagebox.showinfo("Success", "Patient added successfully.")
        patient_window.destroy()
        
    Button(patient_window, text="Add Patient", command=add_patient).pack(pady=20)
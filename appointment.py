from tkinter import *
from tkinter import messagebox
import database

# appointment screen

def open_appointment_page(main_screen):
    appointment_window =Toplevel(main_screen)
    appointment_window.title("Add appointment")
    appointment_window.geometry("300x300")
    
    Label(appointment_window, text="doctor_id:").pack(pady=5)
    doctor_id_entry = Entry(appointment_window)
    doctor_id_entry.pack(pady=5)
    
    Label(appointment_window, text="patient_id:").pack(pady=5)
    patient_id_entry = Entry(appointment_window)
    patient_id_entry.pack(pady=5)

    Label(appointment_window, text="date:").pack(pady=5)
    date_entry = Entry(appointment_window)
    date_entry.pack(pady=5)

    
    def add_appointment():
        doctor_id = doctor_id_entry.get()
        patient_id = patient_id_entry.get()
        date = date_entry.get()
        
        database.add_appointment(doctor_id,patient_id,date) # add to database
    
        messagebox.showinfo("Success", "appointment added successfully.")
        appointment_window.destroy()
        
    Button(appointment_window, text="Add appointment", command=add_appointment).pack(pady=20)
    
def assign_doctor_to_patient(patient_id):
    # get doctors info and current appointment number from database
    doctors = database.get_all_doctors()
        
    
    for doctor in doctors:
        print(doctor)  # debug line

        
        # doctor değişkenini kontrol edin
        if isinstance(doctor, tuple):
            doctor_id = doctor[0]  # id
            doctor_name = doctor[1]  # name
            max_appointments = doctor[2]  # max_appointments
        elif isinstance(doctor, dict):
            doctor_id = doctor['id']
            doctor_name = doctor['name']
            max_appointments = doctor['max_appointments']
        else:
            continue  # Eğer doktor beklenmedik bir türse, bu döngüyü atlayın

        appointments = database.get_appointments_count_by_doctor(doctor_id)

        if appointments < max_appointments:
            date = "2024-10-11"  # örnek randevu tarihi
           
            
            database.add_appointment(doctor_id, patient_id, date)
            return f"Appointment assigned to {doctor_name} on {date}"

    return "No available doctors. Schedule is full"
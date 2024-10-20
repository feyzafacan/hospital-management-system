import sqlite3

# function that starts database connection
def connect():
    return sqlite3.connect('hospital.db')

# to create database tables
def init_db():
    conn = connect()
    cursor = conn.cursor()
    
    # doctors table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS doctors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            contact TEXT NOT NULL
        )           
        ''')
    # Add max_appointments column if it doesn't exist
    try:
        cursor.execute("ALTER TABLE doctors ADD COLUMN max_appointments INTEGER DEFAULT 5")
    except sqlite3.OperationalError:
        pass  # max_appointments already exists
    
    # patients table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            symptoms TEXT NOT NULL,
            contact TEXT NOT NULL,
            address TEXT NOT NULL
        )           
        ''')
        
    # appointments table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            doctor_id INTEGER,
            patient_id INTEGER,
            date TEXT NOT NULL,
            FOREIGN KEY(doctor_id) REFERENCES doctors(id),
            FOREIGN KEY(patient_id) REFERENCES patients(id)
            
        )           
        ''')
    
    conn.commit()
    conn.close()
    
# functions that add doctors, patients and appointments to the database

def add_doctor(name,department,contact):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO doctors (name,department, contact) VALUES (?,?,?)',(name,department,contact))
    conn.commit()
    conn.close()

def add_patient(name,symptoms,contact, address):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO patients (name,symptoms,contact, address) VALUES (?,?,?,?)',(name,symptoms,contact, address))
    conn.commit()
    conn.close()
    

def add_appointment(doctor_id, patient_id, date):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO appointments (doctor_id, patient_id, date) VALUES (?,?,?)',(doctor_id, patient_id, date))
    conn.commit()
    conn.close()
        
        
# to get total number of doctors

def get_total_doctors():
    conn =  connect()  # open database collection
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM doctors')
    total_doctors = cursor.fetchone()[0] # get result
    conn.close()
    return total_doctors

# to get total number of patients

def get_total_patients():
    conn =  connect()  # open database collection
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM patients')
    total_patients = cursor.fetchone()[0] # get result
    conn.close()
    return total_patients

# to get total number of appointments

def get_total_appointments():
    conn =  connect()  # open database collection
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM appointments')
    total_appointments = cursor.fetchone()[0] # get result
    conn.close()
    return total_appointments

# update number of doctors
def get_doctor_count():
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM doctors")  # doctors tablosunun adını kontrol edin
    count = cursor.fetchone()[0]
    conn.close()
    return count

# reset table for code testing 

def reset_tables():
    conn = connect()
    cursor = conn.cursor()

    # Tablolardaki tüm verileri sil
   # cursor.execute('DELETE FROM doctors')
    #cursor.execute('DELETE FROM patients')
    #cursor.execute('DELETE FROM appointments')
    
    cursor.execute("DROP TABLE IF EXISTS appointments")
    cursor.execute("DROP TABLE IF EXISTS patients")
    cursor.execute("DROP TABLE IF EXISTS doctors")
    
    # Tabloları yeniden oluştur
    init_db()  

    conn.commit()
    conn.close()
    
    
def get_recent_doctors():
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT name, department, contact, 'Active' as status FROM doctors ORDER BY id DESC LIMIT 5")
    recent_doctors = cursor.fetchall()
    conn.close()
    
    return recent_doctors

def get_recent_patients():
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT name, symptoms, contact, address, 'Active' as status FROM patients ORDER BY id DESC LIMIT 5")
    recent_patients = cursor.fetchall()
    conn.close()
    
    return recent_patients

def get_all_doctors():
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, max_appointments FROM doctors")  # max_appointments sütununu kaldırdık
    return cursor.fetchall() 

def get_appointments_count_by_doctor(doctor_id):
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM appointments WHERE doctor_id = ?",(doctor_id,))
    result = cursor.fetchone()[0]
    conn.close()
    return result


def add_appointment(doctor_id,patient_id,date):
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO appointments  (doctor_id, patient_id, date) VALUES (?, ?, ?)",
                   (doctor_id, patient_id, date))
    conn.commit()

def get_all_appointments():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT doctor_id, patient_id, date FROM appointments")
    appointments = cursor.fetchall()
    conn.close()
    return appointments

def get_all_patients():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients")
    patients = cursor.fetchall()  # Tüm hasta kayıtlarını al
    conn.close()
    return patients
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
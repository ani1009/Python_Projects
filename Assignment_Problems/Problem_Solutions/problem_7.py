'''
Create a class called "Patient" that represents a patient in a healthcare system. The class
should have the following features:
● A constructor method that takes the patient's name, age, and medical condition as
parameters and initializes them.
● A method called "schedule_appointment" that takes the name of a doctor and a date as
parameters and schedules an appointment for the patient with the specified doctor on
the given date.
● A method called "display_patient_info" that prints the patient's name, age, and medical
condition.
Write the Patient class and demonstrate its usage by creating an instance of the class,
scheduling an appointment, and displaying the patient's information.
'''

class Patient:
    def __init__(self,name,age,medical_condition):
        self.name = name
        self.age = age
        self.medical_condition = medical_condition

    def schedule_appointment(self,doctor_name,appointment_date):
        print(f"Scheduling an Appointment for {self.name} With {doctor_name} On {appointment_date}.")

    def display_patient_info(self):
        print(f"Patient Information:\nName: {self.name}\nAge: {self.age}\nMedical Condition: {self.medical_condition}")

patient1 = Patient("Mr.Gaurav Patil", 35, "Dibetis")

patient1.schedule_appointment("Dr. Deshpande", "28-06-2023")

patient1.display_patient_info()





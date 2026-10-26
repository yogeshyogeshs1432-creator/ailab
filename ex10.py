
appointments = []

def book_appointment():
    print("\n--- Book Hospital Appointment ---")

    name = input("Enter patient name: ")
    age = input("Enter patient age: ")

    print("\nAvailable Doctors:")
    print("1. Dr. Arun - Cardiologist")
    print("2. Dr. Priya - Dentist")
    print("3. Dr. Kumar - General Physician")

    choice = input("Select doctor (1-3): ")

    doctors = {
        "1": "Dr. Arun - Cardiologist",
        "2": "Dr. Priya - Dentist",
        "3": "Dr. Kumar - General Physician"
    }

    if choice not in doctors:
        print("Invalid doctor selection!")
        return

    date = input("Enter appointment date (DD-MM-YYYY): ")
    time = input("Enter appointment time: ")

    appointment = {
        "name": name,
        "age": age,
        "doctor": doctors[choice],
        "date": date,
        "time": time
    }

    appointments.append(appointment)

    print("\nAppointment booked successfully!")
    print("Patient:", name)
    print("Doctor:", doctors[choice])
    print("Date:", date)
    print("Time:", time)


def view_appointments():
    print("\n--- All Appointments ---")

    if len(appointments) == 0:
        print("No appointments found.")
        return

    for i, appointment in enumerate(appointments, start=1):
        print("\nAppointment", i)
        print("Patient Name:", appointment["name"])
        print("Age:", appointment["age"])
        print("Doctor:", appointment["doctor"])
        print("Date:", appointment["date"])
        print("Time:", appointment["time"])


def main():
    while True:
        print("\n===== HOSPITAL APPOINTMENT SYSTEM =====")
        print("1. Book Appointment")
        print("2. View Appointments")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_appointment()
        elif choice == "2":
            view_appointments()
        elif choice == "3":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice! Try again.")


main()

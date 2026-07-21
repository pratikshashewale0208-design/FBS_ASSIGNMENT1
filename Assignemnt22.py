#Assignment22
mport pickle


# Employee class
class Emp:

    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def __str__(self):
        return f"ID: {self.eid}, Name: {self.ename}, Basic Salary: {self.basic}"


# File name
FILE_NAME = "employee.dat"


# Read all records from file
def read_records():
    try:
        with open(FILE_NAME, "rb") as file:
            return pickle.load(file)

    except FileNotFoundError:
        return []


# Write records to file
def write_records(records):
    with open(FILE_NAME, "wb") as file:
        pickle.dump(records, file)


# Add a new employee
def add_record():

    records = read_records()

    eid = int(input("Enter Employee ID: "))

    # Check duplicate ID
    for emp in records:
        if emp.eid == eid:
            print("Employee ID already exists!")
            return

    ename = input("Enter Employee Name: ")
    basic = float(input("Enter Basic Salary: "))

    emp = Emp(eid, ename, basic)

    records.append(emp)

    write_records(records)

    print("Employee record added successfully!")


# Search employee using ID
def search_record():

    records = read_records()

    eid = int(input("Enter Employee ID to search: "))

    for emp in records:
        if emp.eid == eid:
            print("\nEmployee Found")
            print(emp)
            return

    print("Employee record not found!")



def delete_record():

    records = read_records()

    eid = int(input("Enter Employee ID to delete: "))

    for emp in records:
        if emp.eid == eid:
            records.remove(emp)
            write_records(records)

            print("Employee record deleted successfully!")
            return

    print("Employee record not found!")


# Edit employee using ID
def edit_record():

    records = read_records()

    eid = int(input("Enter Employee ID to edit: "))

    for emp in records:

        if emp.eid == eid:

            print("Current Details:")
            print(emp)

            emp.ename = input("Enter New Employee Name: ")
            emp.basic = float(input("Enter New Basic Salary: "))

            write_records(records)

            print("Employee record updated successfully!")
            return

    print("Employee record not found!")


# Display all employees
def display_records():

    records = read_records()

    if len(records) == 0:
        print("No employee records found!")
        return

    print("\nAll Employee Records")
    print("--------------------")

    for emp in records:
        print(emp)


# Main menu
def main():

    while True:

        print("\n===== Employee Management System =====")
        print("1. Add Record")
        print("2. Search Record")
        print("3. Delete Record")
        print("4. Edit Record")
        print("5. Display All Records")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_record()

        elif choice == "2":
            search_record()

        elif choice == "3":
            delete_record()

        elif choice == "4":
            edit_record()

        elif choice == "5":
            display_records()

        elif choice == "6":
            print("Program Ended.")
            break

        else:
            print("Invalid choice! Please try again.")



main()


class Student:
    def __init__(self, name, major, year, id, email):
        self.name = name
        self.major = major
        self.year = year
        self.id = id
        self.email = email
        self.assignments = []
        self.deleted_assign =[]
        self.finished_assign = []
        self.exams = []
    def __repr__(self):
        print(self.name, "\n", self.major, "\n", self.year, "\n", self.id, "\n", self.email)

    def update_name(self, name):
        self.name = name1
        print("Done! \n")
    def get_name(self):
        print(self.name)

    def update_major(self, major):
        self.major = major1
        print("Done! \n")
    def get_major(self):
        print(self.major)

    def update_year(self, year):
        self.year = year1
    def get_year(self):
        print(self.year)

    def update_id(self, id):
        self.id = id1
        print("Done! \n")
    def get_id(self):
        print(self.id)

    def update_email(self, email):
        self.email = email1
        print("Done! \n")
    def get_email(self):
        print(self.email)



    def get_assign():
        print(self.assignments)
    def add_assign(self, assign):
        self.assignments.append(assign + "\n")
        print("Done! \n")
    def delete_assign(self, assign):
        if assign in assignments:
            self.deleted_assign.append(assign + "\n")
            self.assignments.remove(assign)
            print("Done! \n")
    def mark_assign_done(self, assign):
        if assign in assignments:
            self.finished_assign.append(assign + "DONE \n")
            self.assignments.remove(assign)
            print("Done! \n")
    def get_finished_assign():
        print(self.finished_assign)



name1 = input("Name: ")
major1 = input("Major: ")
year1 = input("Year?")
id1 = input("Andrew ID: ")
email1 = input("Andrew Email: ")

student1 = Student(name1, major1, year1, id1, email1)



print("\n\n Welcome to your profile!")

while True:
    command = input("\n Type what you want to access. Alternatively, type 'help'. \n \n")


    if command == "help":
        print("\n \n Those are your options: \n \n \t My Profile \n\t My Assignments \n\t My Exams \n\t Contacts \n")
        command = input("\n What do you need help in? \n")
    elif command == "my profile":
        print("\n \n Here are your options: \n")
        command = input("\t 1.Change Data \n\t 2.View Data \n")
        if command == "change data":
            print("\n \n What would you like to change?: \n")
            command = input("\t 1.Name \n\t 2.Major \n\t 3.Year \n\t 4.Andrew ID \n\t 5.Andrew Email \n \n ")
            if command == "name" or 1:
                name1 = input("New name: \n")
                student1.update_name(name1)
            elif command == "major" or 2:
                major1 = input("New major: \n")
                student1.update_major(major1)
            elif command == "year" or 3:
                year1 = input("Current year: \n")
                student1.update_year(year1)
            elif command == "andrew id" or 4:
                id1 = input("New ID: \n")
                student1.update_id(id1)
            elif command == "andrew email" or 5:
                email1 = input("New email: \n")
                student1.update_email(email1)
            else:
                break
        elif command == "view data":
            print(student1.__repr__())
    elif command == "my assignments":
        print("\n \n Here are your options: \n")
        command = input("\t 1.View Assignments \n\t 2.Add Assignment \n\t 3.Remove Assignmnet \n\t 4.Mark Done \n\t 5.View Finished Assignments \n \n")
        if command == "view assignments":
            student1.get_assign
        elif command == "add assignment" or 2:
            assign = input("What is the new assignment? \n")
            student1.add_assign(assign)
        elif command == "remove assignment" or 3:
            assign = input("Which assignment? \n")
            student1.delete_assign(assign)
        elif command == "mark done" or 4:
            assign = input("Which assignment? \n")
            student1.mark_assign_done(assign)
        elif command == "view finished assignments" or 5:
            student1.get_finished_assign







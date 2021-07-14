from tkinter import *
import webbrowser

# class Student:
#     def __init__(self, name, major, year, id, email):
#         self.name = name
#         self.major = major
#         self.year = year
#         self.id = id
#         self.email = email
#         self.assignments = []
#         self.deleted_assign =[]
#         self.finished_assign = []
#         self.exams = []
#     def __repr__(self):
#         print(self.name, "\n", self.major, "\n", self.year, "\n", self.id, "\n", self.email)

#     def update_name(self, name):
#         self.name = name1
#         print("Done! \n")
#     def get_name(self):
#         print(self.name)

#     def update_major(self, major):
#         self.major = major1
#         print("Done! \n")
#     def get_major(self):
#         print(self.major)

#     def update_year(self, year):
#         self.year = year1
#     def get_year(self):
#         print(self.year)

#     def update_id(self, id):
#         self.id = id1
#         print("Done! \n")
#     def get_id(self):
#         print(self.id)

#     def update_email(self, email):
#         self.email = email1
#         print("Done! \n")
#     def get_email(self):
#         print(self.email)



#     def get_assign():
#         print(self.assignments)
#     def add_assign(self, assign):
#         self.assignments.append(assign + "\n")
#         print("Done! \n")
#     def delete_assign(self, assign):
#         if assign in assignments:
#             self.deleted_assign.append(assign + "\n")
#             self.assignments.remove(assign)
#             print("Done! \n")
#     def mark_assign_done(self, assign):
#         if assign in assignments:
#             self.finished_assign.append(assign + "DONE \n")
#             self.assignments.remove(assign)
#             print("Done! \n")
#     def get_finished_assign():
#         print(self.finished_assign)


root = Tk()
root.geometry("500x500")

frame0 = Frame(root).pack(side=TOP)
frame1 = Frame(root).pack(side=BOTTOM)
frame2 = Frame(root).pack(side=BOTTOM)


name_var=StringVar()
major_var=StringVar()
year_var=StringVar()
id_var=StringVar()
email_var=StringVar()


assignments_var=[]
removed_assignments_var=[]

hello = Label(frame0, text="Hello! Enter your information bellow:").pack()

e_name = Entry(frame1, textvariable = name_var, width=20)
e_name.pack()
e_name.insert(0, "Name")
e_major = Entry(frame1, textvariable = major_var, width=20)
e_major.pack()
e_major.insert(0, "Major")
e_year = Entry(frame1, textvariable = year_var, width=20)
e_year.pack()
e_year.insert(0, "Year")
e_id = Entry(frame1, textvariable = id_var, width=20)
e_id.pack()
e_id.insert(0, "Andrew ID")
e_email = Entry(frame1, textvariable = email_var, width=20)
e_email.pack()
e_email.insert(0, "Andrew Email")


def proceed():
    global window1
    window1 = Toplevel(root)
    window1.title("Options")
    window1.geometry("200x200")
    Label(window1, text="Welcome! What would you like to do?").pack(side=TOP)
    b_profile = Button(window1, text="My Profile", command=my_profile).pack()
    b_assignments = Button(window1, text="My Assignments", command=my_assignments).pack()
    b_links = Button(window1, text="My Links", command=my_links).pack()

def my_profile():
    global window2
    window2 = Toplevel(root)
    Label(window2, text="Here are your options.").pack()
    Button(window2, text="View Data", command=lambda:[window2.destroy(), view_data()]).pack()
    Button(window2, text="change_data", command=lambda:[window2.destroy(), change_data()]).pack()

def my_assignments():
    global window5
    window5 = Toplevel(root)
    Label(window5, text="Here are your options.").pack()
    Button(window5, text="View My Assignments", command=lambda:[window5.destroy(), view_assignments()]).pack()
    Button(window5, text="Add Assignment", command=lambda:[window5.destroy(), add_assignment()]).pack()
    Button(window5, text="Remove Assignment", command=lambda:[window5.destroy(), remove_assignment()]).pack()

def my_links():
    global window7
    window7 = Toplevel(root)
    Label(window7, text="Here are your options.").pack()
    link = Entry(window7, width=20)
    link.pack()
    Button(window7, text = "This opens Google",command=openweb).pack()




def openweb():
    webbrowser.open(link.get(),new=new)
    

def view_data():
    global window3
    window3 = Toplevel(root)
    Label(window3, text=name_var.get()+"\n"+major_var.get()+"\n"+year_var.get()+"\n"+id_var.get()+"\n"+email_var.get()).pack()
def change_data():
    global window4
    window4 = Toplevel(root)
    e_name = Entry(window4, textvariable = name_var, width=20)
    e_name.pack()
    e_name.insert(0, name_var.get())
    e_major = Entry(window4, width=20)
    e_major.pack()
    e_major.insert(0, major_var.get())
    e_year = Entry(window4, width=20)
    e_year.pack()
    e_year.insert(0, year_var.get())
    e_id = Entry(window4, width=20)
    e_id.pack()
    e_id.insert(0, id_var.get())
    e_email = Entry(window4, width=20)
    e_email.pack()
    e_email.insert(0, email_var.get())
    Button(window4, text="Done.", command=lambda:[window4.destroy(), view_data()]).pack()
def view_assignments():
    global window6
    window6 = Toplevel(root)
    Label(window6, text=assignments_var[0]).pack()
def add_assignment():
    global window6, new_assignment
    window6 = Toplevel(root)
    new_assignment = StringVar()
    e_new_assignment = Entry(window6, textvariable = new_assignment, width=20).pack()
    Button(window6, text="Add.", command=lambda:[window6.destroy(), add_assignment_confirmed()]).pack()
def add_assignment_confirmed():
    assignments_var.append(new_assignment.get()+"\n")
def remove_assignment():
    global window6, chosen_assignment
    window6 = Toplevel(root)
    chosen_assignment = StringVar()
    e_chosen_assignment = Entry(window6, textvariable = chosen_assignment, width=20).pack()
    Button(window6, text="Remove.", command=lambda:[window6.destroy(), remove_assignment_confirmed()]).pack()
def remove_assignment_confirmed():
    if chosen_assignment in assignments_var:
        removed_assignments_var.append(chosen_assignment.get()+"\n")
        assignments_var.delete(chosen_assignment.get)



str


proceed1 = Button(frame2, text="Proceed", command=proceed)
proceed1.pack()




# student1 = Student(name1, major1, year1, id1, email1)



# command = input("\n \n Welcome to your profile! What would you like to do? \n \n")

# while True:

#     if command == "help":
#         print("\n \n Those are your options: \n \n \t My Profile \n\t My Assignments \n\t My Exams \n\t Contacts \n")
#         command = input("\n What do you need help in? \n")
#     elif command == "my profile":
#         print("\n \n Here are your options: \n")
#         command = input("\t 1.Change Data \n\t 2.View Data \n")
#         if command == "change data":
#             print("\n \n What would you like to change?: \n")
#             command = input("\t 1.Name \n\t 2.Major \n\t 3.Year \n\t 4.Andrew ID \n\t 5.Andrew Email \n \n ")
#             if command == "name" or 1:
#                 name1 = input("New name: \n")
#                 student1.update_name(name1)
#             elif command == "major" or 2:
#                 major1 = input("New major: \n")
#                 student1.update_major(major1)
#             elif command == "year" or 3:
#                 year1 = input("Current year: \n")
#                 student1.update_year(year1)
#             elif command == "andrew id" or 4:
#                 id1 = input("New ID: \n")
#                 student1.update_id(id1)
#             elif command == "andrew email" or 5:
#                 email1 = input("New email: \n")
#                 student1.update_email(email1)
#         elif command == "view data":
#             print(student1.__repr__())
#     elif command == "my assignments":
#         print("\n \n Here are your options: \n")
#         command = input("\t 1.View Assignments \n\t 2.Add Assignment \n\t 3.Remove Assignmnet \n\t 4.Mark Done \n\t 5.View Finished Assignments \n \n")
#         if command == "view assignments" or 1:
#             student1.get_assign
#         elif command == "add assignment" or 2:
#             assign = input("What is the new assignment? \n")
#             student1.add_assign(assign)
#         elif command == "remove assignment" or 3:
#             assign = input("Which assignment? \n")
#             student1.delete_assign(assign)
#         elif command == "mark done" or 4:
#             assign = input("Which assignment? \n")
#             student1.mark_assign_done(assign)
#         elif command == "view finished assignments" or 5:
#             student1.get_finished_assign




root.mainloop()


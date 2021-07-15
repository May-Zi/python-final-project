from tkinter import *
import webbrowser




root = Tk()
root.geometry("500x460")
root.configure(bg="#ffe6b3")

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

hello = Label(frame0, text="\n Hello! Enter your information bellow: \n", bg="#ffe6b3", font=("mistral", 23)).pack()

e_name = Entry(frame1, textvariable = name_var, bg="#ffefcc", font=("mistral", 20), justify="center")
e_name.pack(ipady=5, ipadx= 20)
e_name.insert(0, "Name")
e_major = Entry(frame1, textvariable = major_var, bg="#ffefcc", font=("mistral", 20), justify="center")
e_major.pack(ipady=5, ipadx= 20)
e_major.insert(0, "Major")
e_year = Entry(frame1, textvariable = year_var, bg="#ffefcc", font=("mistral", 20), justify="center")
e_year.pack(ipady=5, ipadx= 20)
e_year.insert(0, "Year")
e_id = Entry(frame1, textvariable = id_var, bg="#ffefcc", font=("mistral", 20), justify="center")
e_id.pack(ipady=5, ipadx= 20)
e_id.insert(0, "Andrew ID")
e_email = Entry(frame1, textvariable = email_var, bg="#ffefcc", font=("mistral", 20), justify="center")
e_email.pack(ipady=5, ipadx= 20)
e_email.insert(0, "Andrew Email")


def proceed():
    global window1
    window1 = Toplevel(root)
    window1.title("Options")
    window1.geometry("500x420")
    window1.configure(bg="#ffe6b3")
    Label(window1, text="\n \n Welcome! What would you like to do? \n", bg="#ffe6b3", font=("mistral", 23)).pack(side=TOP)
    b_profile = Button(window1, text="My Profile", command=my_profile, bg="#ffefcc", font=("mistral", 18), width=20).pack()
    b_assignments = Button(window1, text="My Assignments", command=my_assignments, bg="#ffefcc", font=("mistral", 18), width=20).pack()
    b_links = Button(window1, text="My Links", command=my_links, bg="#ffefcc", font=("mistral", 18), width=20).pack()

def my_profile():
    global window2
    window2 = Toplevel(root)
    window2.title("My Profile")
    window2.geometry("500x300")
    window2.configure(bg="#ffe6b3")
    Label(window2, text="\nHere are your options.\n", bg="#ffe6b3", font=("mistral", 23)).pack()
    Button(window2, text="View Data", command=lambda:[window2.destroy(), view_data()], bg="#ffefcc", font=("mistral", 18), width=20).pack()
    Button(window2, text="change_data", command=lambda:[window2.destroy(), change_data()], bg="#ffefcc", font=("mistral", 18), width=20).pack()

def my_assignments():
    global window5
    window5 = Toplevel(root)
    window5.title("My Assignments")
    window5.geometry("500x350")
    window5.configure(bg="#ffe6b3")
    Label(window5, text="\nHere are your options.\n", bg="#ffe6b3", font=("mistral", 23)).pack()
    Button(window5, text="View My Assignments", command=lambda:[window5.destroy(), view_assignments()], bg="#ffefcc", font=("mistral", 18), width=20).pack()
    Button(window5, text="Add Assignment", command=lambda:[window5.destroy(), add_assignment()], bg="#ffefcc", font=("mistral", 18), width=20).pack()
    Button(window5, text="Remove Assignment", command=lambda:[window5.destroy(), remove_assignment()], bg="#ffefcc", font=("mistral", 18), width=20).pack()

def my_links():
    global window7, link
    window7 = Toplevel(root)
    window7.title("My Links")
    window7.geometry("500x550")
    window7.configure(bg="#ffe6b3")
    link=StringVar()
    Label(window7, text="\n Here are your options: \n", bg="#ffe6b3", font=("mistral", 23)).pack()
    Button(window7, text="Canvas", command=canvas, bg="#ffefcc", font=("mistral", 18), width=15).pack(pady=2)
    Button(window7, text="Box", command=box, bg="#ffefcc", font=("mistral", 18), width=15).pack(pady=2)
    Button(window7, text="Health Connect", command=health_connect, bg="#ffefcc", font=("mistral", 18), width=15).pack(pady=2)
    Button(window7, text="Email", command=gmail, bg="#ffefcc", font=("mistral", 18), width=15).pack(pady=2)
    Label(window7, text="\n Or insert custome link here:", bg="#ffe6b3", font=("mistral", 23)).pack(pady=2)
    e_link = Entry(window7, textvariable = link , width=20, bg="#ffefcc", font=("mistral", 20), justify="center")
    e_link.pack(pady=5)
    Button(window7, text = "Go", command=openweb, bg="#ffefcc", font=("mistral", 20), width=15).pack(pady=5)




def openweb():
    webbrowser.open(link.get())
def canvas():
    global canvas_link
    canvas_link = "https://canvas.cmu.edu/"
    webbrowser.open(canvas_link)
def box():
    global box_link
    box_link = "https://cmu.account.box.com/login"
    webbrowser.open(box_link)
def health_connect():
    global health_connect_link
    health_connect_link = "https://healthservices.qatar.cmu.edu/confirm.aspx"
    webbrowser.open(health_connect_link)
def gmail():
    global gmail_link
    gmail_link = "https://mail.google.com/"
    webbrowser.open(gmail_link)


def view_data():
    global window3
    window3 = Toplevel(root)
    window3.geometry("450x450")
    window3.configure(bg="#ffe6b3")
    Label(window3, text="\n Here is your current data: \n", bg="#ffe6b3", font=("mistral", 24)).pack()
    Label(window3, text="name: "+name_var.get()+"\n\n major: "+major_var.get()+"\n\n year: "+year_var.get()+"\n\n andrew id: "+id_var.get()+"\n\n andrew email: "+email_var.get(), bg="#ffefcc", font=("mistral", 20)).pack()
def change_data():
    global window4
    window4 = Toplevel(root)
    window4.geometry("450x320")
    window4.configure(bg="#ffe6b3")
    e_name = Entry(window4, textvariable = name_var, width=20, bg="#ffefcc", font=("mistral", 23), justify="center")
    e_name.pack(pady=5)
    e_major = Entry(window4, textvariable = major_var, width=20, bg="#ffefcc", font=("mistral", 23), justify="center")
    e_major.pack(pady=5)
    e_year = Entry(window4, textvariable = year_var, width=20, bg="#ffefcc", font=("mistral", 23), justify="center")
    e_year.pack(pady=5)
    e_id = Entry(window4, textvariable = id_var, width=20, bg="#ffefcc", font=("mistral", 23), justify="center")
    e_id.pack(pady=5)
    e_email = Entry(window4, textvariable = email_var, width=20, bg="#ffefcc", font=("mistral", 23), justify="center")
    e_email.pack(pady=5)
    Button(window4, text="Done.", command=lambda:[window4.destroy()], bg="#fff7e6", font=("mistral", 18), width=15).pack(pady=5)
def view_assignments():
    global window6
    window6 = Toplevel(root)
    window6.geometry("500x300")
    window6.configure(bg="#ffe6b3")
    Label(window6, text=assignments_var, bg="#ffe6b3", font=("mistral", 24)).pack()
def add_assignment():
    global window6, new_assignment
    window6 = Toplevel(root)
    window6.geometry("500x300")
    window6.configure(bg="#ffe6b3")
    Label(window6, text="\n Write the title of the \n new assignment below: ", bg="#ffe6b3", font=("mistral", 20)).pack()
    new_assignment = StringVar()
    e_new_assignment = Entry(window6, textvariable = new_assignment, width=20, bg="#ffefcc", font=("mistral", 23), justify="center").pack(pady=15)
    Button(window6, text="Add.", command=lambda:[window6.destroy(), add_assignment_confirmed()], bg="#fff7e6", font=("mistral", 18), width=15).pack(pady=15)
def add_assignment_confirmed():
    assignments_var.append(new_assignment.get())
    assignments_var.append(",")
def remove_assignment():
    global window6, chosen_assignment
    window6 = Toplevel(root)
    window6.geometry("500x300")
    window6.configure(bg="#ffe6b3")
    Label(window6, text="\n Write the title of \n the assignment below: ", bg="#ffe6b3", font=("mistral", 20)).pack()
    chosen_assignment = StringVar()
    e_chosen_assignment = Entry(window6, textvariable = chosen_assignment, width=20, bg="#ffefcc", font=("mistral", 23), justify="center").pack(pady=15)
    Button(window6, text="Remove.", command=lambda:[window6.destroy(), remove_assignment_confirmed()], bg="#fff7e6", font=("mistral", 18), width=15).pack(pady=15)
def remove_assignment_confirmed():
    if chosen_assignment.get() in assignments_var:
        removed_assignments_var.append(chosen_assignment.get())
        assignments_var.remove(chosen_assignment.get())
        assignments_var.remove(",")



str


proceed1 = Button(frame2, text="  Proceed  ", command=proceed, bg="#fff7e6", font=("mistral", 18))
proceed1.pack()





root.mainloop()


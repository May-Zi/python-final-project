from tkinter import *

#root = Tk()
#root.mainloop()
#Label(root, text="")
#Button(root, text="", command= sth, fg="", bg="", state=DISABLED, padx=50, pady=50)
#.pack
#.grid


#TO DO LIST
#method that once a button is pressed, deactivates it

root = Tk()
root.geometry("500x500")

#FRAME??


names = []

# CLASS FOR PLAYERS??
class Player: 
	def __init__(self, name):
		self.name = name

	def add_user(self, name):
		user = Player(name)
		names.insert(0, user)

e = Entry(root)
e.grid(row=5, column=5)



#while True:
#	add_user()
while True:
	names.add_user(e.get)
	e.delete(0, END)
	ask_players = input("Anyone else?")
	if ask_players == "no":
		break
	elif ask_players != "no" or "yes":
		print("only yes and no answers are recognized.")




title = Label(root, text="square game thingie??", font=("Helvetica", 16)).grid(row=0, column=0)


button1 = Button(root, text=":D", padx=20, pady=20).grid(row=2, column=0)
button2 = Button(root, text=":D", padx=20, pady=20).grid(row=2, column=1)
button3 = Button(root, text=":D", padx=20, pady=20).grid(row=2, column=2)
button4 = Button(root, text=":D", padx=20, pady=20).grid(row=2, column=3)
button5 = Button(root, text=":D", padx=20, pady=20).grid(row=3, column=0)
button6 = Button(root, text=":D", padx=20, pady=20).grid(row=3, column=1)
button7 = Button(root, text=":D", padx=20, pady=20).grid(row=3, column=2)
button8 = Button(root, text=":D", padx=20, pady=20).grid(row=3, column=3)
button9 = Button(root, text=":D", padx=20, pady=20).grid(row=4, column=0)
button10 = Button(root, text=":D", padx=20, pady=20).grid(row=4, column=1)
button11 = Button(root, text=":D", padx=20, pady=20).grid(row=4, column=2)
button12 = Button(root, text=":D", padx=20, pady=20).grid(row=4, column=3)


# ASK FOR PLAYER NUMBER (print "too many" if necessary)
# ASK WHETHER THEY'D LIKE COMPUTER INPUT (if players are >1)
# ASK FOR USER NAME




root.mainloop()
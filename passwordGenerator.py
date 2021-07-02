import tkinter as tk
import random
from tkinter import *
root = Tk()
root.geometry("450x120")
root.title("Random Password Generator")
# creating string variable to store input
l = tk.StringVar()
ev = tk.StringVar()

def genPassword():
	entry.delete(0,END)
	passVar = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
	lenOfPassword = int(l.get())
	extra = str(ev.get()).split(",")
	passVar += extra
	password = ""

	for i in range(lenOfPassword):
		temp = random.randint(0, len(passVar)-1)
		password += passVar[temp]
	entry.insert(10, password)
	# passcode.configure(text="Password: "+password)

def copyToClipboard(event):
	root.clipboard_clear()
	pw = entry.get()
	root.clipboard_append(pw)

length = Label(root,text = "Length of password:")
length.grid(row=0,sticky="e")
entryLength = Entry(root,textvariable=l)
entryLength.grid(row=0,column=1)

extraValue = Label(root,text = "Extra(seprated by ','):")
extraValue.grid(row=1,sticky="e")
entryextraValue = Entry(root,textvariable=ev)
entryextraValue.grid(row=1,column=1)

sub_button = Button(root, text = "Genrate",command = genPassword)
sub_button.grid(row=3, column=0)

quit = Button(root,text="Quit",command=root.quit)
quit.grid(row=3,column=1)

passcode = Label(root,text="Password: ")
passcode.grid(row=2,sticky="e")

entry = Entry(root)
entry.grid(row=2,column=1)

copyButton = Button(root,text="Copy")
copyButton.grid(row=3, column=2)
copyButton.bind("<Button-1>", copyToClipboard)
root.mainloop()
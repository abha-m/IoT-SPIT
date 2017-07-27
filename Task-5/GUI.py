""" 
Download tkinter for python using sudo apt-get install python3-tk
"""

from tkinter import *
from tkinter import filedialog

myString = ""		#The Message String goes in this variable
dirname = ""		#The directory goes here

def show_entry_fields():
   print("Message: %s\n" % (e1.get("1.0",END)))
   
   global myString
   myString=(str(e1.get("1.0",END)))
   #print(myString)
   
def upload():
	global dirname
	dirname = filedialog.askopenfilename()
	allDir = dirname.split("/")
	global label
	fileName = allDir[len(allDir)-1]
	label.config(text=str(fileName))


def show_all():
	print("Message : %s" % myString)
	print("Directory : %s" % dirname)
	if(textCheck.get()==1):
		print("txt file")
	elif(xlsxCheck.get()==1):
		print("xlsx file")
	else:
		print("csv file")		


master = Tk()
master.title("Messages")
Label(master, 
		text="Message",
		fg="red",
		bg="sky blue").grid(row=0)

Label(master,text="File Format :").grid(row=1)
label=Label(master)
label.grid(row=6,column=1)

textCheck=IntVar()		#is 1 if file is txt, 0 otherwise
xlsxCheck = IntVar()		#is 1 if file is xlsx, 0 otherwise
csvCheck = IntVar()		#is 1 if file is Csv, 0 otherwise
Checkbutton(master, text="TEXT", variable=textCheck).grid(row=1,column=1, sticky=W)
Checkbutton(master, text="XLSX", variable=xlsxCheck).grid(row=2,column=1, sticky=W)
Checkbutton(master, text="CSV", variable=csvCheck).grid(row=3,column=1, sticky=W)

e1 = Text(master,font=('Verdana',20),height=10,width=12)

e1.grid(row=0, column=1)

Button(master, text='Quit', command=master.quit).grid(row=5, column=0, sticky=W, pady=4)
Button(master, text='Post Message', command=show_entry_fields).grid(row=5, column=1, sticky=W, pady=4)
Button(master, text='Upload File', command=upload).grid(row=6, column=0, sticky=W, pady=4)
Button(master, text='Show All', command=show_all).grid(row=6, column=1, sticky=W, pady=4)

mainloop( )

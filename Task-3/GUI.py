""" 
Download tkinter for python using sudo apt-get install python3-tk
"""

from tkinter import *
from tkinter import filedialog

myString = ""		#The Message String goes in this variable
dirname = ""		#The directory goes here
myData = dict()		#Dictionary of Name:Number
myList=[]			#List of Numbers
mainList=[]

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

def accept():
	global myList
	global myData
	if(typeCheck.get()==2):
		import csv
		global myString
		myString=(str(e1.get("1.0",END)))
		with open(dirname) as csvfile:
			readCSV = csv.reader(csvfile, delimiter=',')
			for row in readCSV:
				#print(row)
				tempList=row[0].split(":")
				myData[tempList[0]]=tempList[1]
			print(myData)
	if(typeCheck.get()==1):
		with open(dirname) as f:
			polyShape = []
			for line in f:
				line = line.split() # to deal with blank
				if line:
					print(line)
					line=str(line)
					line = line[2:len(line)-2]
					#print(line)             # lines (ie skip them)
					polyShape.append(line)
			for i in polyShape:
				print (i)
				tempList=i.split(":")
				myData[tempList[0]]=tempList[1]
			print(myData)
	if(typeCheck.get()==3):
		from xlrd import open_workbook
		wb = open_workbook(dirname)
		sheet = wb.sheet_by_index(0)
		numList=[]
		for i in sheet.col_values(0):
			numList.append(int(i))
		myData=dict(zip(numList,sheet.col_values(1)))

def on():
	accept()
	if(Checkall.get()==1):
		global mainList
		mainlist=[]
		for i in myData:
			mainList.append(myData[i])
		print("All Selected")
		print(mainList)
		listbox.delete(0,END)
		for i in myData:
			listbox.insert(END,i)


master = Tk()
listbox = Listbox(master)
listbox.grid(row=10)
#top = Toplevel() 
master.title("Messages")
Label(master, 
		text="Message",
		fg="red",
		bg="sky blue").grid(row=0)

Label(master,text="File Format :").grid(row=2)
Label(master,text="Select Names:").grid(row=6)
#Label(master,text=mainList).grid(row=10)
label=Label(master)
label.grid(row=20,column=1)
typeCheck=IntVar()		#is 1 if file is txt, 2 if csv, 3 if xlsx,0 otherwise
Checkall=IntVar()
var=StringVar()
Radiobutton(master, text="TEXT", variable=typeCheck,value=1).grid(row=2,column=1)
Radiobutton(master, text="XLSX", variable=typeCheck,value=3).grid(row=3,column=1)
Radiobutton(master, text="CSV", variable=typeCheck,value=2).grid(row=4,column=1)
Checkbutton(master, text="Select all", variable=Checkall,onvalue=1,offvalue=0).grid(row=7,column=0,sticky=W)

e1 = Text(master,font=('Verdana',14),height=4,width=16)
e1l = Text(master,font=('Verdana',12),height=1,width=16)

e1.grid(row=0, column=1)
e1l.grid(row=6, column=1)
#listbox.insert(END,"sdgsdg")
listbox.insert(END, "Selected names")
Button(master, text='Quit', command=master.quit).grid(row=8, column=0, sticky=W, pady=4)
Button(master, text='Post Message', command=on).grid(row=8, column=1, sticky=W, pady=4)
Button(master, text='Upload File', command=upload).grid(row=5, column=0, sticky=W, pady=4)
Button(master, text='Show All', command=show_all).grid(row=5, column=1, sticky=W, pady=4)

#listbox.pack()
mainloop( )




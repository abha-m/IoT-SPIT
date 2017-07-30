""" 
Download tkinter for python using sudo apt-get install python3-tk
"""

from tkinter import *
from tkinter import filedialog
import serial
import time
import sys

myString = ""	
dirname = ""
myData = dict()
myList=[]
mainList=[]

ser = serial.Serial(port='/dev/ttyS0',baudrate=115200,timeout=2)
ser.write(bytes("AT\r",'UTF-8'))
ser.write(bytes("AT+CSQ\r",'UTF-8'))

   
def uploadAndImport():
	global dirname
	dirname = filedialog.askopenfilename()
	allDir = dirname.split("/")
	global label
	fileName = allDir[len(allDir)-1]
	label.config(text=str(fileName))
	getFromFile()
	global mainList
	nameBox.delete(0,END)
	for i in myData:
		nameBox.insert(END,i)
		

def getFromFile():
	global myList
	global myData
	if(typeCheck.get()==2):
		import csv
		global myString
		myString=(str(e1.get("1.0",END)))
		with open(dirname) as csvfile:
			readCSV = csv.reader(csvfile, delimiter=',')
			for row in readCSV:
				tempList=row[0].split(":")
				myData[tempList[0]]=tempList[1]
	if(typeCheck.get()==1):
		with open(dirname) as f:
			polyShape = []
			for line in f:
				line = line.split()
				if line:
					line=str(line)
					line = line[2:len(line)-2]
					polyShape.append(line)
			for i in polyShape:
				tempList=i.split(":")
				myData[tempList[0]]=tempList[1]
	if(typeCheck.get()==3):
		from xlrd import open_workbook
		wb = open_workbook(dirname)
		sheet = wb.sheet_by_index(0)
		numList=[]
		for i in sheet.col_values(0):
			numList.append(int(i))
		myData=dict(zip(numList,sheet.col_values(1)))

def post():
	ser.write(bytes('AT+CMGF=1\r','UTF-8'))
	print(ser.read(20))
	
	global mainList
	global myString
	myString = str(messageText.get("1.0",END))
	for i in mainList:
		phoneNumber = i
		time.sleep(2)
		ser.write(bytes('''AT+CMGS="''' + phoneNumber + '''"\r''','UTF-8'))
		time.sleep(2)
		ser.write(bytes(myString + "\r",'UTF-8'))
		time.sleep(2)
		ser.write(bytes(chr(26),'UTF-8'))
		time.sleep(2)
		
def selectNames():
	global selBox
	global nameBox
	global mainList
	tempList=[]
	tempNames=[]
	tempList=nameBox.curselection()
	mainlist=[]
		
	for i in tempList:
		tempNames.append(nameBox.get(i))	
	for i in myData:
		if(i in tempNames):
			selBox.insert(END,i)
			mainList.append(myData[i])						

def selectAll():
	for i in myData:
		mainList.append(myData[i])
		selBox.insert(END,i)

def search():
	global myData
	global mainList
	queryString = str(searchText.get("1.0",CURRENT))
	qLen = len(queryString)
	
	for i in myData:
		sliceOfData = i[:qLen]
		if(queryString == sliceOfData):
			selBox.insert(END,i)
			mainList.append(myData[i])

master = Tk()
master.title("Messages")
Label(master, 
		text="Message",
		fg="red",
		bg="sky blue").grid(row=0)
Label(master,text="File Format :").grid(row=2)
Label(master,text="Imported").grid(row=6,column=0)
Label(master,text="Selected:").grid(row=6,column=1)
label=Label(master)
label.grid(row=5,column=1)
typeCheck=IntVar()
Checkall=IntVar()
var=StringVar()
Radiobutton(master, text="TEXT", variable=typeCheck,value=1).grid(row=2,column=1)		
Radiobutton(master, text="XLSX", variable=typeCheck,value=3).grid(row=3,column=1)
Radiobutton(master, text="CSV", variable=typeCheck,value=2).grid(row=4,column=1)
Button(master, text='Select All', command=selectAll).grid(row=8, column=1, pady=4)
messageText = Text(master,font=('Verdana',14),height=4,width=16)
searchText = Text(master,font=('Verdana',12),height=1,width=14)
messageText.grid(row=0, column=1)
searchText.grid(row=9, column=0)
nameBox = Listbox(master,selectmode=MULTIPLE)
nameBox.insert(END, "Imported names")
nameBox.grid(row=7,column=0)
selBox = Listbox(master)
selBox.grid(row=7,column=1)
Button(master, text='Select Names', command=selectNames).grid(row=8, column=0, pady=4)
Button(master, text='Post Message', command=post).grid(row=10, column=0, pady=4)
Button(master, text='Upload File', command=uploadAndImport).grid(row=5, column=0, pady=4)
Button(master, text='Select searched', command=search).grid(row=9, column=1, pady=4)
Button(master, text='Quit', command=master.quit).grid(row=10, column=1, pady=4)
mainloop( )

<<<<<<< HEAD
from xlrd import open_workbook
wb = open_workbook('f.xlsx')
sheet = wb.sheet_by_index(0)
for i in sheet.col_values(0):
=======
from xlrd import open_workbook
wb = open_workbook('f.xlsx')
sheet = wb.sheet_by_index(0)
for i in sheet.col_values(0):
>>>>>>> 6955c080d9a647ce01af530b8fbe5147aa14ca6b
	print (int(i))
from xlrd import open_workbook
wb = open_workbook('f.xlsx')
sheet = wb.sheet_by_index(0)
for i in sheet.col_values(0):
	print (int(i))
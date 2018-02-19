import openpyxl

wb = openpyxl.load_workbook('./Corpus/36.xlsx')
ws = wb.active
text_column = ws['AB']
rows = len(text_column)

for row in range(rows):
	print (text_column[row].value)

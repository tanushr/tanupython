
 
import xlrd 
  
# Give the location of the file 
loc = ("oo.xls") 
  
# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)
sheet.cell_value(0,0) 
for i in range(sheet.nrows):  
	print(sheet.cell_value(i, 0)) 


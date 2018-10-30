import panda as pd

writer = pd.ExcelWriter('farm_data.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')

workbook = writer.book
worksheet = writer.sheets['Sheet1']

chart = workbook.add_chart({'type': 'column'})

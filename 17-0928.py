import xlrd
file_name = '你好.xls'
#  打开XLS 文件
book = xlrd.open_workbook(file_name)
#  打开工作目录
try:
    sh = book.sheet_by_name('1')

except:
    print("文件中没有这个Sheet")

value = sh.row_values(6)
while True:
    if '' in value:
        value.remove('')
    else:
        break
print(value)

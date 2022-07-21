'''Собираем эксель-файлы из директории с обходом поддиректорй в один файл'''
# Import `os` 
import os
import openpyxl

# Retrieve current working directory (`cwd`)
cwd = os.getcwd()
print(cwd)

#result xl file 
wb_out = openpyxl.Workbook()
ws_out = wb_out.active


# Change directory 
os.chdir("C:/Users/user/Documents/База")
cwd = os.getcwd()
print(cwd)

# List all files and directories in current directory
# iterate over files in
# that directory
for root, dirs, files in os.walk(cwd):
    for filename in files:
        xl = os.path.join(root, filename)
        if '.xlsx' in xl:
            print(xl)
            wb = openpyxl.load_workbook(xl,read_only=True, data_only=True)
            sheet = wb.active
            data = sheet.values
            
            for row in data:
                row += (filename, dirs)
                ws_out.append(row)
    
wb_out.save('out1.xlsx')  
wb_out.close()

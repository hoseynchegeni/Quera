import re
a = input()
string = re.findall(r'\d+.(.+)',a)
numeric = re.findall(r'(\d+)',a)
b = 'copy of '*int(numeric[0])+string[0]
print(b)
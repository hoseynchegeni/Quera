import re
a=input()
resault = re.findall(r'(.)+....',a)
X = resault[0].upper()
if X == 'G':
    print('rahat baash')
elif X=='R' or resault[0]=='Y':
    print('nakhor lite')

a = input()
red = 0 
yellow = 0 
green = 0
for i in a:
    if i == 'R':
        red += 1
        
    if i == 'Y':
        yellow += 1
    
    if i == 'G':
        green += 1

if red >= 3 :
    print('nakhor lite')
elif yellow >= 2 and red >= 2 :
    print('nakhor lite')
elif green == 0 :
    print('nakhor lite')
else:
    print('rahat baash')



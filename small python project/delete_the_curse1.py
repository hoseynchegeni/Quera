text = input('>>>')
text = text.split()
for i in range(len(text)):
    if text[i].upper() == 'FUCK' or text[i].upper() == 'SHIT'or text[i].upper() == 'ASS' or text[i].upper() == 'FUCKER':
        text [i] = '****'
print(*text,sep=" ")







             
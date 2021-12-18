def game(number):
    x = str(number)
    if int(x[1]) >int(x[0]):
        number = int(x[1]) - int(x[0])
        return(number)
    else:
        number = int(x[0]) - int(x[1])
        return (number)






howmuch = int(input('сколько есть у бота:  '))
while True:
    inputvalue = input('msg: ')

    checkvalue = howmuch == 0
    if checkvalue == True:
        answer='ans: не'
    else:
        answer='ans: +'

    if inputvalue == 'есть че?':
        print(answer)
    elif inputvalue == 'привет':
        print('ans: привет')

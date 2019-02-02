howmuch = int(input('how much:  '))
while True:
    inputvalue = input('msg: ')

    checkvalue = howmuch == 0
    if checkvalue == True:
        answer='ans: no'
    else:
        answer='ans: yes'

    if inputvalue == 'you have?':
        print(answer)

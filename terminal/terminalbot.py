import random
howmuch = 0
answeryes = ['+', 'угу', 'да', 'ага', ')']
answerno = ['нет', 'не', '-', '(', 'неа']
answerhello = ['привет', 'здарова', 'йо', 'ку']
while True:
    inputvalue = input('msg: ')

    checkvalue = howmuch == 0
    if checkvalue == True:
        answer=random.choice(answerno)
    else:
        answer=random.choice(answeryes)

    if inputvalue == 'есть че?':
        print(answer)
    elif inputvalue == 'есть че':
        print(answer)
    elif inputvalue == 'есть?':
        print(answer)
    elif inputvalue == 'привет':
        print(random.choice(answerhello))
    elif inputvalue == '***дать 1':
        howmuch = howmuch + 1
        print('msg: спс')

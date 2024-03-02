while True:
    print("Calculator [+ - * / ^] Exit: 'x' ")
    action = input('Action: ')
    if action == 'x':
        break

    result = 0
    n1 = float(input('Number 1: '))
    n2 = float(input('Number 2: '))

    if action == '+':
        result = n1 + n2
    elif action == '-':
        result = n1 - n2
    elif action == '*':
        result = n1 * n2
    elif action == '//':
        if n2 == 0:
            print("NO")
            continue
        result = n1 // n2
    elif action == '^':
        result = n1 ^ n2
    else:
        print("Unknown command")

    print('Result = ', result)

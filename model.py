def elevate_expression(expression):
    try:
        result = str(eval(expression, {}, {}))
    except:
        result = 'ERROR'

    return result


if __name__ == '__main__':
    while True:
        expression = input('Введіть вираз: ')
        if expression == 'exit':
            break
        print(f'Результат обчислення виразу {expression} = {elevate_expression(expression)}')

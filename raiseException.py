print('Введите положительное число')
x = int(input())
if x < 0:
    raise Exception('Число не является положительным')
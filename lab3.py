# -*- coding: utf-8 -*-

from uncertainties import ufloat

x = 1874014748.18092000
y = x * 10**(-10)
c = x + y
c9 = round(c, 9)  # округление переменной c до 9 знаков после запятой
# использование функции ufloat из библиотеки uncertainties для +-
z = ufloat(x, 10**(-8))
k = round(x)

print('Y = ', y)
print('C = ', c)
print('C` = ', c9)
print('Z = ', z)
print('K = ', k)

y2 = z * 10**(-10)  # умножение с ошибкой

absErrY = abs(y - y2)  # абсолютная ошибка для умножения
relErrY = absErrY / y  # относительная ошибка для умножения

absErrC = abs(c - c9)  # относительная ошибка для сложения
relErrC = absErrC / c  # относительная ошибка для сложения

absErrK = abs(x-k)  # абсолютная ошибка для округления
relErrK = absErrK / x  # относительная ошибка для округления

print('Результат умножения с ошибкой = ', y2)
print('Абсолютная ошибка для умножения = ', absErrY)
print('Относительная ошибка для умножения = ', relErrY)
print('Абсолютная ошибка для сложения = ', absErrC)
print('Относительная ошибка для сложения = ', relErrC)
print('Абсолютная ошибка для округления = ', absErrK)
print('Относительная ошибка для округления = ', relErrK)

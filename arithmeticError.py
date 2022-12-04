try:
    k = 1 / 0
except ArithmeticError:
    k = 0
print(k)

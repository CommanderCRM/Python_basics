a = [1, 2, 3] # переменная a теперь указывает на значения списка, которые хранятся в памяти
print (a)

iterationCount = 0
    
def iterations(f, x0, a, b, eps, f1):
    global iterationCount # ссылаемся на переменную, которая задана глобально
    iterationCount += 1 # изменяется глобальная переменная, на которую ссылались выше
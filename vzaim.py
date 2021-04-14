def one(n): 
    if n>0:
        print('Hello')
        two(n)

def two(n):
    print('world')
    one(n-1)

one(5)


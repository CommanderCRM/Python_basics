from contracts import contract


@contract(a='int,>0', b='int,>0')
def sum(a, b):
    return a + b


print(sum(3, 4))

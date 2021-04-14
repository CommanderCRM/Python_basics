def rev(x):
    if x > 0:
        print(x%10)
        rev(x//10)
rev(359)
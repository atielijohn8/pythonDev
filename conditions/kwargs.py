def super_function(*args,**kwargs):

    print(*args)
    print(args)
    total = 0
    for items in kwargs.values():
        total += items

    return sum(args) + total

print (super_function(1,2,3,4,5,num1 = 5, num2 = 10))
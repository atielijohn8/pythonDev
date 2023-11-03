def sum(num1,num2):
    def another_func(n1,n2):
        return n1 + n2#not exiting/(definition not exec)
    return another_func(num1,num2)
    #return atomatically exits the function
    print('hello')
    
total = sum(10,10)
print(total)
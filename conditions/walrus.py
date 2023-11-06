a ='hureeeeeeeee'

if ((n:=len(a)) > 10):
    print(f"too long {n} elements")#replace the len
    while ((n := len(a)) > 1 ):
        print(n)
        a = a[:-1]

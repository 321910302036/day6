def fibonacciNumbers(n):
    f1 = 0
    f2 =  1
    if (n==1):
        print(f1)
    else:
        print(f1)
        print(f2)
    for x in range(2,n):
        print(f2, end = " ")
        next=f1 + f2
        f1 = f2
        f2=next
        print(next)
fibonacciNumbers(10)





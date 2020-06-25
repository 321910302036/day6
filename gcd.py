def gcd(a,b):
    if (b==0):
        return a
    return gcd(b, a%b)
a=45
b=32
if(gcd(a,b)):
    print('gcd of', a , 'and',b,'is',gcd(a, b))
else:
    print('not found') 


NumList=[]
Even_count = 0
odd_count  = 0

Number = int(input("please enter the total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("please enter the value of %d Element : "%i))
    NumList.append(value)
for  j in range(Number):
    if(NumList[j] % 2 == 0):
        Even_count = Even_count + 1
    else:
        odd_count = odd_count + 1
print("\nTotal Number of Even Numbers in this List = ",Even_count)
print("\nTotal Number of Odd  Numbers in this List= ",odd_count)

a=int(input("Enter first number\n"))
b=int(input("Enter second number\n"))
number=0
for num in range(a,b):
    if num%2==0 and num%3==0 and num%4==0 and num%5==0 and num%6==0 and num%7==0 and num%8==0 and num%9==0 and num%10==0:
        print (num)
        number+=1
else:
    print("Enter second number bigger then")

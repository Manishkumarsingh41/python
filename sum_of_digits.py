num = int(input('Enere any number:-'))
sum = 0
while num != 0:
    rem=num%10
    num//= 10 
    sum= sum+rem
    print("sum of digits: ",sum)


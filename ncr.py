def fact(num):
 if num == 0:
  return 1
 else:
  return num * fact(num-1)
n = int(input("Enter the value of N : "))
r = int(input("Enter the value of R (R cannot be negative or greaterthan N): "))
nCr = fact(n)/(fact(r)*fact(n-r))
print(n,'c',r," = ","%d"%nCr,sep="")
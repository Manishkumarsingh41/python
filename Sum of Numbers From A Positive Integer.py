num_int=int(input("Enter number from where you want to sum\n",))
int_init=num_int
sum=0
while num_int > 0:
    sum+=num_int
    num_int-=1
print(int_init)
print(sum)
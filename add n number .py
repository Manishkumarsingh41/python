#A python program to add n numbers accepted from the user

n = int(input("How many numbers do you want to add? :- "))
total = 0
for i in range(n):
 num = float(input("Enter a number:- "))
 total += num
print("The sum of the entered numbers is:-", total)


#OUTPUT
# How many numbers do you want to add? :- 5
# Enter a number:- 1
# Enter a number:- 2
# Enter a number:- 3
# Enter a number:- 4
# Enter a number:- 5
# The sum of the entered numbers is:- 15.0
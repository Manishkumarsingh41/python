# ********** FOR LOOP **********

# Loop from 1 to 9 with step 2
for i in range(1, 10, 2):
    print(i)

# Output:
# 1
# 3
# 5
# 7
# 9

print("------")

# Loop from 10 down to 2 (exclusive), step -1
for i in range(10, 1, -1):
    print(i)

# Output:
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2

print("------")

# Loop through each character in the string
str = "Manish kumar singh"
for i in str:
    print(i)

# Output:
# M
# a
# n
# i
# s
# h
#  
# k
# u
# m
# a
# r
#  
# s
# i
# n
# g
# h

# ********** WHILE LOOP **********

# Print numbers from 0 to 4
count = 0
while count < 5:
    print(count)
    count += 1

# Output:
# 0
# 1
# 2
# 3
# 4

print("------")

# Only prints 0 because next count becomes odd
count = 0
while count % 2 == 0:
    print(count)
    count += 1

# Output:
# 0

# ********** BREAK **********

# Stops loop when i == 5
for i in range(10):
    if i == 5:
        break
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4

# ********** CONTINUE **********

# Skips even numbers
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# Output:
# 1
# 3
# 5
# 7
# 9

# ********** PASS **********

# pass is a placeholder, does nothing
for i in range(5):
    if i == 3:
        pass
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4

# ********** NESTED LOOP **********

for i in range(3):
    for j in range(2):
        print(f"i: {i} and j: {j}")

# Output:
# i: 0 and j: 0
# i: 0 and j: 1
# i: 1 and j: 0
# i: 1 and j: 1
# i: 2 and j: 0
# i: 2 and j: 1

# ********** SUM USING WHILE LOOP **********

n = 10
sum = 0
count = 1

while count <= n:
    sum += count
    count += 1

print("The sum of first 10 natural numbers is:", sum)

# Output:
# The sum of first 10 natural numbers is: 55

# ********** SUM USING FOR LOOP **********

n = 10
sum = 0

for i in range(n + 1):
    sum += i

print("The sum of first 10 natural numbers is:", sum)

# Output:
# The sum of first 10 natural numbers is: 55

# ********** PRIME NUMBERS BETWEEN 1 TO 20 **********

for num in range(1, 20):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

# Output:
# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19

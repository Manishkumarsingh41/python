def lcm(a, b):
    # Find the greater number
    max_num = max(a, b)
    
    # Start from the greater number and check if it is divisible by both a and b
    while True:
        if max_num % a == 0 and max_num % b == 0:
            lcm = max_num
            break
        max_num += 1
    
    return lcm

# Test the function
num1 = 12
num2 = 18
result = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is {result}")

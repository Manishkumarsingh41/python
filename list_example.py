# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements in the list
print(my_list[0])  # Output: 1
print(my_list[2])  # Output: 3

# Adding elements to the list
my_list.append(6)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# Removing elements from the list
my_list.remove(3)
print(my_list)  # Output: [1, 2, 4, 5, 6]

# Modifying elements in the list
my_list[0] = 0
print(my_list)  # Output: [0, 2, 4, 5, 6]

# Looping through the list
for item in my_list:
    print(item)

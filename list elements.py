# Creating a list
my_list = [1, 2, 3, 4, 5, 6]

# Accessing elements in the list
print(my_list[0]) 
print(my_list[2]) 

# Adding elements to the list
my_list.append(6)
print(my_list)  

# Removing elements from the list
my_list.remove(4)
print(my_list)  

# Modifying elements in the list
my_list[0] = 0
print(my_list) 

# Looping through the list
for item in my_list:
    print(item)
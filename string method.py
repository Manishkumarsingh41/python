the_string = "North India"
print(the_string.rjust(15))  
print(the_string.ljust(15, "*"))  
center_plus = the_string.center(14, "+")  
print(center_plus)
print(the_string.lstrip("South"))
print(center_plus.rstrip("+"))  
print(center_plus.strip("+"))  
print(the_string.replace("North", "South"))  
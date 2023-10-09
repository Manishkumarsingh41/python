name=input("Enter employe name:-")
year_of_join=int(input("Enter year when you join the company"))
exp=2023-year_of_join
if exp>=5:
    print("You are elegible for bonous")
    sal=int(input("Enter your salery:-"))
    bonous_percentage = float(input("Enter bonous percentage:-"))    
    bonous=sal*(bonous_percentage/100)+sal
    print("The salary of ",name,"after adding bonous is ",bonous,)
else:
    print("You are not elegible for bonous ")

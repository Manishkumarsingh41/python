person_dict = {}
name = input("Enter the person's name: ")
dob = input("Enter the person's date of birth (in YYYY-MM-DD format): ")
if name in person_dict:
    print(f"The date of birth for {name} is {person_dict[name]}.")
else:
    
    person_dict[name] = dob
    print(f"Added {name} with date of birth {dob} to the dictionary.")


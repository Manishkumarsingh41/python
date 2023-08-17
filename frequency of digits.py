num = input("Enter a number : ")
print("The number entered is :", num)
uniqDig = set(num)
for elem in uniqDig:
 print(elem, "occurs", num.count(elem), "times")

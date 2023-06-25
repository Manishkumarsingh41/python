celsius = int(input("Enter an integer that represents celsius.\n"))
def fahrenheit(celsius):
    return (18 * celsius + 320) / 10
print("The Fahrenheit equivalent of " + str(celsius) + " degrees Celsius is " + str(fahrenheit(celsius)) + ".")
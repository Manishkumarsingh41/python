# num=int(input("Enter any number\n"))
# if num<0:
#     n=num*(-1)
#     print("The absolute number is ",n)
# else:
#     print("This is already absolute number ")


# Collect the product name, price, and quantity of each product purchased.
product_names = []
product_prices = []
product_quantities = []

while True:
    product_name = input("Enter the product name: ")
    product_price = float(input("Enter the product price: "))
    product_quantity = int(input("Enter the product quantity: "))

    product_names.append(product_name)
    product_prices.append(product_price)
    product_quantities.append(product_quantity)

    # Check if the user wants to enter another product.
    answer = input("Do you want to enter another product? (y/n): ")
    if answer == "n":
        break

# Calculate the total cost of the purchase.
total_cost = 0
for i in range(len(product_names)):
    total_cost += product_prices[i] * product_quantities[i]

# Apply any discounts that may apply.
for i in range(len(product_names)):
    if product_quantities[i] >= 10:
        discount = 0.1 * product_prices[i]
        product_prices[i] -= discount

# Print a receipt for the customer.
print("Receipt")
print("---------------------------------")
for i in range(len(product_names)):
    print("Product Name:", product_names[i])
    print("Product Price:", product_prices[i])
    print("Product Quantity:", product_quantities[i])
    print("Discount:", discount)
print("---------------------------------")
print("Total Cost:", total_cost)
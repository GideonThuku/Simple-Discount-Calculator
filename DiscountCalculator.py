# 🎯 Simple Discount Calculator 🎯
# This program helps you know the final price after discount.

# Function to do the discount math
def calculate_discount(price, discount_percent):
    # check if discount is 20% or more
    if discount_percent >= 20:
        # find how much money is cut off
        discount_amount = price * (discount_percent / 100)
        # new price after discount
        final_price = price - discount_amount
        return final_price
    else:
        # if discount less than 20, no discount given
        return price


# 👉 Start of the program
print("--------------------------------------------------------------------")
print("             Weclome to Our Simple Discount Calculator")
print("--------------------------------------------------------------------")

# ask the user for inputs
price = float(input(         "Please type the original price: "))
discount = float(input(      "Please type the discount percent: "))

# call the function
final_price = calculate_discount(price, discount)

# showingthe answer below
print("----------------------------------------------------------------------")
if discount >= 20:
    print(f"              Great news, you have a {discount}% discount!")
    print(f"                   Final Price = {final_price:.2f}")
else:
    print(                "Bad news, discount is too small. No discount given.")
    print(f"               Final Price = {final_price:.2f}")
print("----------------------------------------------------------------------")
print("          Thank you for using our simple discount checker!")
print("----------------------------------------------------------------------")
print("               Program made by Gideon, PLP Academy")

# def calculate_discount(price, discount_percent):
#     if discount_percent >= 20:
#        return price * (1 - discount_percent / 100)
#     else:
#          return price

# try:
#     original_price = float(input("Enter the original price: "))
#     discount = float(input("Enter the discount percentage: "))
#     final_price = calculate_discount(original_price, discount)
#     if discount_percent>= 20:
#         print(f"The final price after a {discount_percent}% discount is: ${final_price:.2f}")
#     else:
#         print(f"No discount applied. The price remains: ${final_price:.2f}")
# except ValueError:
#     print("Invalid input. Please enter numeric values for price and discount percentage.")

def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount if the discount is 20% or higher.
    
    Parameters:
    price (float): Original price of the item
    discount_percent (float): Discount percentage to apply
    
    Returns:
    float: Final price after discount (or original price if discount < 20%)
    """
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    else:
        return price

# Prompt user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    # Calculate final price
    final_price = calculate_discount(original_price, discount_percentage)
    
    # Display result
    if discount_percentage >= 20:
        print(f"Final price after {discount_percentage}% discount: ${final_price:.2f}")
    else:
        print(f"No discount applied. Original price: ${original_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount.")
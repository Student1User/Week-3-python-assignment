def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    
    If the discount percentage is 20% or higher, apply the discount.
    Otherwise, return the original price.
    """
    if discount_percent >= 20:
        final_price = price - (price * (discount_percent / 100))
        return final_price
    else:
        return price  # No discount applied

# Get user input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate final price
    final_price = calculate_discount(price, discount_percent)

    # Print the result
    if discount_percent >= 20:
        print(f"✅ Discount applied! The final price is: ${final_price:.2f}")
    else:
        print(f"❌ No discount applied. The price remains: ${price:.2f}")

except ValueError:
    print("⚠️ Invalid input! Please enter numeric values for price and discount.")

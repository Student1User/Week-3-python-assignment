# Discount Calculator - Week 3 Python Assignment (PLP Academy)

## 📌 Overview
This is a simple **Discount Calculator** application built using **Python**. The program allows users to enter the original price of an item and a discount percentage. If the discount is **20% or more**, it applies the discount and displays the final price; otherwise, it retains the original price.

This assignment is part of **Week 3 of the Python Module** at **PLP Academy**.

---

## 🛠 Features
- **User input handling** to accept original price and discount percentage.
- **Input validation** to ensure only valid numbers are entered.
- **Simple and user-friendly CLI design**.
- **Error handling** using exception handling for invalid inputs.

---

## 📜 How It Works
1. The user enters the **original price** and the **discount percentage**.
2. The program checks if the discount is **20% or more**.
3. If the condition is met, the program calculates the discounted price and displays it.
4. If the discount is **less than 20%**, the original price is displayed without modification.
5. If invalid input is provided (e.g., text instead of numbers), an error message appears.

---

## 🖥️ Installation & Usage
### 🔹 Prerequisites
- Python 3.x installed on your system.

### 🔹 Running the Program
1. **Clone or Download the Repository:**
   ```sh
   git clone https://github.com/your-username/week3-discount-calculator.git
   cd week3-discount-calculator
   ```
2. **Run the Python Script:**
   ```sh
   python discount_calculator.py
   ```

---

## 📝 Code Breakdown
### 🔹 Function: `calculate_discount()`
This function retrieves the user's inputs, validates them, and calculates the discounted price if applicable.
```python
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
```

---

## 🤖 Example Usage
| Original Price | Discount % | Final Price |
|---------------|------------|------------|
| $100          | 25%        | $75.00      |
| $50           | 15%        | $50.00      |
| $200          | 30%        | $140.00     |

---

## 🛠 Technologies Used
- **Python 3** 🐍

---

## 🏆 Assignment Details
- **Course:** Software Engineering
- **Module:** Python
- **Week:** 3
- **Institution:** PLP Academy

---

## 🔗 Contributing
If you’d like to contribute, feel free to fork this repository and submit a pull request! 🎉

---

## 📜 License
This project is open-source and available under the **MIT License**.

---

## 📞 Contact
For any questions or feedback, reach out to me via:
- Email: magachi.emmanuel@students.jkuat.ac.ke


🚀 **Happy Coding & Keep Learning!** 🎯


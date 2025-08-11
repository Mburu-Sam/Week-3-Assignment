# Discount Calculator

A simple Python program that calculates the final price after applying a discount if the discount percentage is 20% or higher.

## Features

- Calculates discounted price for discounts of 20% or more
- Returns original price for discounts below 20%
- Handles user input validation
- Displays formatted currency output
- Clear messaging about whether discount was applied

## Requirements

- Python 3.x

## How to Use

1. Run the program:
   ```bash
   python discount_calculator.py
   ```

2. Enter the original price when prompted
3. Enter the discount percentage when prompted

The program will display either:
- The discounted price (if discount ≥ 20%)
- The original price (if discount < 20%)

## Example Usage

```
Enter the original price of the item: 1000
Enter the discount percentage: 25
Final price after 25% discount: ksh700.00
```

```
Enter the original price of the item: 1000
Enter the discount percentage: 15
No discount applied. Original price: ksh1000.00
```

## Error Handling

The program will display an error message if:
- Non-numeric values are entered for price or discount
- Input cannot be converted to a float

## Code Structure

The main function `calculate_discount(price, discount_percent)`:
- Takes price and discount percentage as parameters
- Returns discounted price if discount ≥ 20%
- Returns original price otherwise

The program includes proper input validation and formatted output.
```

This README provides:
- Clear description of what the program does
- Installation/running instructions
- Usage examples
- Information about features and error handling
- Overview of the code structure
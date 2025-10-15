# Total revenue calculation from sales data

def total_revenue(sales):
    total = 0
    for item in sales:
        total += item["price"] * item["quantity"]
    return total

# Example data
sales_data = [
    {"item": "Pen", "price": 20, "quantity": 3},
    {"item": "Book", "price": 200, "quantity": 2},
    {"item": "Bag", "price": 800, "quantity": 1}
]

print("Total Revenue:", total_revenue(sales_data))

# Output: Total Revenue: 1260

# Explanation

# The function total_revenue iterates through each sale item,
# calculates the revenue for that item (price * quantity),
# and sums it up to get the total revenue.
# The output shows the total revenue calculated from the sales data.

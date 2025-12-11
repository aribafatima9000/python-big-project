# Store Billing System Project

print("===== Welcome to Mini Store =====")

# Product list (dictionary)
products = {
    "Chips": 50,
    "Juice": 120,
    "Chocolate": 80,
    "Biscuits": 40
}

print("\nAvailable Products:")
for p, price in products.items():
    print(f"{p} - Rs {price}")

print("\n------ Your Purchase ------")

cart = {}
total_bill = 0

# User purchase
for p, price in products.items():
    qty = int(input(f"{p} quantity (0 if not buying): "))
    
    if qty > 0:
        item_total = qty * price
        cart[p] = item_total
        total_bill += item_total

# Discount Logic
discount = 0
if total_bill >= 500:
    discount = total_bill * 0.10   # 10% discount
elif total_bill >= 300:
    discount = total_bill * 0.05   # 5% discount

final_amount = total_bill - discount

# Print Receipt
print("\n===== Final Receipt =====")
for item, amount in cart.items():
    print(f"{item}: Rs {amount}")

print("-----------------------------")
print(f"Total Bill: Rs {total_bill}")
print(f"Discount: Rs {discount}")
print(f"Final Amount to Pay: Rs {final_amount}")
print("Thank you for shopping!")





# Student Marks Manager Project

students = [
    {"name": "Ali", "math": 78, "science": 82, "english": 70},
    {"name": "Sana", "math": 55, "science": 60, "english": 58},
    {"name": "Hira", "math": 90, "science": 92, "english": 88},
    {"name": "Usman", "math": 40, "science": 38, "english": 45}
]

print("Name\tMath\tSci\tEng\tTotal\tPercent\tGrade\tStatus")
print("-" * 70)

for s in students:
    # Total
    total = s["math"] + s["science"] + s["english"]
    
    # Percentage
    percent = total / 3
    
    # Grade logic
    if percent >= 80:
        grade = "A"
    elif percent >= 70:
        grade = "B"
    elif percent >= 60:
        grade = "C"
    elif percent >= 50:
        grade = "D"
    else:
        grade = "F"
        
    # Pass/Fail logic
    status = "Pass" if percent >= 50 else "Fail"
    
    # Print output
    print(f"{s['name']}\t{s['math']}\t{s['science']}\t{s['english']}\t{total}\t{percent:.1f}%\t{grade}\t{status}")

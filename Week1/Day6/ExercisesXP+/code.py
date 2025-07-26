import math

# Exercise 1:
student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}

# a
student_averages = {}

for name, grade in student_grades.items():
    student_averages.update({name : (sum(grade) / len(grade))})
print(student_averages)

# b
student_letter_grades = {}
for name, grade in student_averages.items():
    if grade >= 90:
        student_letter_grades.update({name : 'A'})
    elif grade >= 80 and grade <= 89:
        student_letter_grades.update({name : 'B'})
    elif grade >= 70 and grade <= 79:
        student_letter_grades.update({name : 'C'})
    elif grade >= 60 and grade <= 69:
        student_letter_grades.update({name : 'D'})
    else:
        student_letter_grades.update({name : 'F'})
print(student_letter_grades)

class_average = 0
for grade in student_averages.values():
    class_average += grade
print(class_average/len(student_averages.values()))

# Print the name of each student, their average grade, and their letter grade.

for name, grades in student_grades.items():
    print(f"{name}'s average grade is {student_averages[name]} and letter grade is {student_letter_grades[name]}")

# Exercise 2: Advanced Data Manipulation and Analysis

sales_data = [
    {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
    {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
    {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
    {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
    {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
    {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
    {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
]

# 1
total_sales = {}
for entry in sales_data:
    product = entry["product"]
    cost = entry["price"] * entry["quantity"]
    if product in total_sales:
        total_sales[product] += cost
    else:
        total_sales[product] = cost

print(total_sales)

# 2
customer_spend = {}
for entry in sales_data:
    customer = entry["customer_id"]
    cost = entry["price"] * entry["quantity"]
    if customer in customer_spend:
        customer_spend[customer] += cost
    else:
        customer_spend[customer] = cost

print(customer_spend)

# 3
for transaction in sales_data:
    total_price = transaction["price"] * transaction["quantity"]
    transaction.update({'total_price' : total_price})

# 4
high_value_transactions = [transaction for transaction in sales_data if transaction['total_price'] > 500]
print(high_value_transactions)

# 5
purchase_counts = {}
for transaction in sales_data:
    customer_id = transaction["customer_id"]
    if customer_id not in purchase_counts:
        purchase_counts[customer_id] = 1
    else:
        purchase_counts[customer_id] += 1
    
loyal_customers = [customer_id for customer_id, count in purchase_counts.items() if customer_id >= 2]
print(loyal_customers)
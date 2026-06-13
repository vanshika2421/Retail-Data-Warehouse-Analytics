# import pyodbc
# from faker import Faker

# fake = Faker()

# conn = pyodbc.connect(
#     "Driver={ODBC Driver 17 for SQL Server};"
#     "Server=(localdb)\\MSSQLLocalDB;"
#     "Database=RetailDWProject;"
#     "Trusted_Connection=yes;"
# )

# cursor = conn.cursor()

# for _ in range(100):
#     cursor.execute("""
#         INSERT INTO Customers
#         (FirstName, LastName, Email, Phone, City, State)
#         VALUES (?, ?, ?, ?, ?, ?)
#     """,
#     fake.first_name(),
#     fake.last_name(),
#     fake.email(),
#     fake.msisdn()[:10],
#     fake.city(),
#     fake.state()
#     )

# conn.commit()

# print("100 Customers Inserted Successfully!")

# conn.close()


# import pyodbc
# import random

# conn = pyodbc.connect(
#     "Driver={ODBC Driver 17 for SQL Server};"
#     "Server=(localdb)\\MSSQLLocalDB;"
#     "Database=RetailDWProject;"
#     "Trusted_Connection=yes;"
# )

# cursor = conn.cursor()

# products = [
#     ("Laptop", "Electronics", "Dell"),
#     ("Mouse", "Electronics", "Logitech"),
#     ("Keyboard", "Electronics", "HP"),
#     ("Monitor", "Electronics", "Samsung"),
#     ("Headphones", "Electronics", "Sony"),

#     ("T-Shirt", "Clothing", "Nike"),
#     ("Jeans", "Clothing", "Levis"),
#     ("Jacket", "Clothing", "Puma"),
#     ("Shoes", "Clothing", "Adidas"),

#     ("Sofa", "Home", "IKEA"),
#     ("Dining Table", "Home", "IKEA"),
#     ("Bed", "Home", "Wakefit"),
#     ("Chair", "Home", "Godrej"),

#     ("Football", "Sports", "Nike"),
#     ("Cricket Bat", "Sports", "SG"),
#     ("Tennis Racket", "Sports", "Yonex")
# ]

# for product_name, category, brand in products:

#     cost_price = random.randint(500, 50000)

#     unit_price = int(cost_price * random.uniform(1.2, 1.6))

#     cursor.execute("""
#         INSERT INTO Products
#         (ProductName, Category, Brand, UnitPrice, CostPrice)
#         VALUES (?, ?, ?, ?, ?)
#     """,
#     product_name,
#     category,
#     brand,
#     unit_price,
#     cost_price)

# conn.commit()

# print("Products Inserted Successfully!")

# conn.close()



# import pyodbc
# import random
# from datetime import datetime, timedelta

# conn = pyodbc.connect(
#     "Driver={ODBC Driver 17 for SQL Server};"
#     "Server=(localdb)\\MSSQLLocalDB;"
#     "Database=RetailDWProject;"
#     "Trusted_Connection=yes;"
# )

# cursor = conn.cursor()

# statuses = [
#     "Delivered",
#     "Pending",
#     "Cancelled",
#     "Shipped"
# ]

# for _ in range(500):

#     customer_id = random.randint(1, 200)

#     order_date = datetime.now() - timedelta(
#         days=random.randint(1, 365)
#     )

#     total_amount = random.randint(1000, 50000)

#     status = random.choice(statuses)

#     cursor.execute("""
#         INSERT INTO Orders
#         (
#             CustomerID,
#             OrderDate,
#             OrderStatus,
#             TotalAmount
#         )
#         VALUES (?, ?, ?, ?)
#     """,
#     customer_id,
#     order_date,
#     status,
#     total_amount)

# conn.commit()

# print("500 Orders Inserted Successfully!")

# conn.close()

# import pyodbc
# import random

# conn = pyodbc.connect(
#     "Driver={ODBC Driver 17 for SQL Server};"
#     "Server=(localdb)\\MSSQLLocalDB;"
#     "Database=RetailDWProject;"
#     "Trusted_Connection=yes;"
# )

# cursor = conn.cursor()

# # Get Products
# cursor.execute("""
# SELECT ProductID, UnitPrice
# FROM Products
# """)

# products = cursor.fetchall()

# # Generate 3 items per order
# for order_id in range(1, 501):

#     selected_products = random.sample(products, 3)

#     for product in selected_products:

#         product_id = product[0]
#         unit_price = float(product[1])

#         quantity = random.randint(1, 5)

#         line_total = quantity * unit_price

#         cursor.execute("""
#             INSERT INTO OrderItems
#             (
#                 OrderID,
#                 ProductID,
#                 Quantity,
#                 UnitPrice,
#                 LineTotal
#             )
#             VALUES (?, ?, ?, ?, ?)
#         """,
#         order_id,
#         product_id,
#         quantity,
#         unit_price,
#         line_total)

# conn.commit()

# print("1500 OrderItems Inserted Successfully!")

# conn.close()



import pyodbc
import random

conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=(localdb)\\MSSQLLocalDB;"
    "Database=RetailDWProject;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Cash"
]

cursor.execute("""
SELECT OrderID, TotalAmount
FROM Orders
""")

orders = cursor.fetchall()

for order in orders:

    order_id = order[0]
    amount = float(order[1])

    payment_method = random.choice(payment_methods)

    cursor.execute("""
        INSERT INTO Payments
        (
            OrderID,
            PaymentMethod,
            Amount
        )
        VALUES (?, ?, ?)
    """,
    order_id,
    payment_method,
    amount)

conn.commit()

print("Payments Inserted Successfully!")

conn.close()
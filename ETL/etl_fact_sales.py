import pyodbc

# Source Connection (OLTP)
source_conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=(localdb)\\MSSQLLocalDB;"
    "Database=RetailDWProject;"
    "Trusted_Connection=yes;"
)

# Target Connection (Data Warehouse)
target_conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=(localdb)\\MSSQLLocalDB;"
    "Database=RetailDW;"
    "Trusted_Connection=yes;"
)

source_cursor = source_conn.cursor()
target_cursor = target_conn.cursor()

# Extract data from OLTP
source_cursor.execute("""
SELECT
    o.OrderDate,
    o.CustomerID,
    oi.ProductID,
    p.PaymentMethod,
    oi.Quantity,
    oi.LineTotal
FROM Orders o
INNER JOIN OrderItems oi
    ON o.OrderID = oi.OrderID
INNER JOIN Payments p
    ON o.OrderID = p.OrderID
""")

sales = source_cursor.fetchall()

for row in sales:

    date_key = int(row.OrderDate.strftime("%Y%m%d"))

    # CustomerKey Lookup
    target_cursor.execute("""
        SELECT CustomerKey
        FROM DimCustomer
        WHERE CustomerID = ?
    """, row.CustomerID)

    customer_key = target_cursor.fetchone()[0]

    # ProductKey Lookup
    target_cursor.execute("""
        SELECT ProductKey
        FROM DimProduct
        WHERE ProductID = ?
    """, row.ProductID)

    product_key = target_cursor.fetchone()[0]

    # PaymentKey Lookup
    target_cursor.execute("""
        SELECT PaymentKey
        FROM DimPayment
        WHERE PaymentMethod = ?
    """, row.PaymentMethod)

    payment_key = target_cursor.fetchone()[0]

    # Insert into FactSales
    target_cursor.execute("""
        INSERT INTO FactSales
        (
            DateKey,
            CustomerKey,
            ProductKey,
            PaymentKey,
            Quantity,
            Revenue
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """,
    date_key,
    customer_key,
    product_key,
    payment_key,
    row.Quantity,
    row.LineTotal
    )

target_conn.commit()

print(f"{len(sales)} FactSales Loaded Successfully!")

source_conn.close()
target_conn.close()
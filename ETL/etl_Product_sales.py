import pyodbc

source_conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=(localdb)\\MSSQLLocalDB;"
    "Database=RetailDWProject;"
    "Trusted_Connection=yes;"
)

target_conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=(localdb)\\MSSQLLocalDB;"
    "Database=RetailDW;"
    "Trusted_Connection=yes;"
)

source_cursor = source_conn.cursor()
target_cursor = target_conn.cursor()

source_cursor.execute("""
SELECT ProductID, ProductName, Category, Brand
FROM Products
""")

products = source_cursor.fetchall()

for product in products:

    target_cursor.execute("""
    INSERT INTO DimProduct
    (
        ProductID,
        ProductName,
        Category,
        Brand
    )
    VALUES (?, ?, ?, ?)
    """,
    product.ProductID,
    product.ProductName,
    product.Category,
    product.Brand
    )

target_conn.commit()

print(f"{len(products)} Products Loaded")

source_conn.close()
target_conn.close()
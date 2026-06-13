
SERVER = "(localdb)\\MSSQLLocalDB"

import pyodbc

# OLTP Connection
source_conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=(localdb)\\MSSQLLocalDB;"
    "Database=RetailDWProject;"
    "Trusted_Connection=yes;"
)

source_cursor = source_conn.cursor()

# DW Connection
target_conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=(localdb)\\MSSQLLocalDB;"
    "Database=RetailDW;"
    "Trusted_Connection=yes;"
)

target_cursor = target_conn.cursor()

# Extract
source_cursor.execute("""
SELECT
    CustomerID,
    FirstName,
    LastName,
    Email,
    City,
    State
FROM Customers
""")

customers = source_cursor.fetchall()

# Load
for customer in customers:

    target_cursor.execute("""
        INSERT INTO DimCustomer
        (
            CustomerID,
            FirstName,
            LastName,
            Email,
            City,
            State
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """,
    customer.CustomerID,
    customer.FirstName,
    customer.LastName,
    customer.Email,
    customer.City,
    customer.State)

target_conn.commit()

print(f"{len(customers)} Customers Loaded")

source_conn.close()
target_conn.close()
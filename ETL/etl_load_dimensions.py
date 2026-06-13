import pyodbc

# Source Connection
source_conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=(localdb)\\MSSQLLocalDB;"
    "Database=RetailDWProject;"
    "Trusted_Connection=yes;"
)

# Target Connection
target_conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=(localdb)\\MSSQLLocalDB;"
    "Database=RetailDW;"
    "Trusted_Connection=yes;"
)

source_cursor = source_conn.cursor()
target_cursor = target_conn.cursor()
print("done")

source_cursor.execute("""
SELECT DISTINCT PaymentMethod
FROM Payments
""")

payments = source_cursor.fetchall()

for payment in payments:

    target_cursor.execute("""
        INSERT INTO DimPayment
        (
            PaymentMethod
        )
        VALUES (?)
    """,
    payment.PaymentMethod
    )

target_conn.commit()

print(f"{len(payments)} Payment Methods Loaded")

print("done")
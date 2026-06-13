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

source_cursor.execute("""
SELECT
    StoreID,
    StoreName,
    City,
    Region
FROM Stores
""")

stores = source_cursor.fetchall()

for store in stores:

    target_cursor.execute("""
        INSERT INTO DimStore
        (
            StoreID,
            StoreName,
            City,
            Region
        )
        VALUES (?, ?, ?, ?)
    """,
    store.StoreID,
    store.StoreName,
    store.City,
    store.Region)

target_conn.commit()

print(f"{len(stores)} Stores Loaded")

source_conn.close()
target_conn.close()
import pyodbc
from datetime import date, timedelta

conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=(localdb)\\MSSQLLocalDB;"
    "Database=RetailDW;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

start_date = date(2025, 5, 30)
end_date = date(2026, 5, 29)

current_date = start_date

while current_date <= end_date:

    date_key = int(current_date.strftime("%Y%m%d"))

    cursor.execute("""
        INSERT INTO DimDate
        (
            DateKey,
            FullDate,
            DayNumber,
            MonthNumber,
            MonthName,
            QuarterNumber,
            YearNumber
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
    date_key,
    current_date,
    current_date.day,
    current_date.month,
    current_date.strftime("%B"),
    ((current_date.month - 1)//3)+1,
    current_date.year
    )

    current_date += timedelta(days=1)

conn.commit()

print("DimDate Loaded Successfully!")

conn.close()
CREATE DATABASE RetailDW;
GO

USE RetailDW;
GO

/* Customers  → DimCustomer
Products   → DimProduct
Payments   → DimPayment
Orders     → DimDate
OrderItems → FactSales 

           DimCustomer
                  |
                  |
DimProduct ---- FactSales ---- DimDate
                  |
                  |
             DimPayment          */


USE RetailDW;
GO

-- Customer Dimension
CREATE TABLE DimCustomer
(
    CustomerKey INT IDENTITY(1,1) PRIMARY KEY,
    CustomerID INT,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    City VARCHAR(50),
    State VARCHAR(50)
);

-- Product Dimension
CREATE TABLE DimProduct
(
    ProductKey INT IDENTITY(1,1) PRIMARY KEY,
    ProductID INT,
    ProductName VARCHAR(100),
    Category VARCHAR(50),
    Brand VARCHAR(50)
);

-- Payment Dimension
CREATE TABLE DimPayment
(
    PaymentKey INT IDENTITY(1,1) PRIMARY KEY,
    PaymentMethod VARCHAR(50)
);

-- Date Dimension
CREATE TABLE DimDate
(
    DateKey INT PRIMARY KEY,
    FullDate DATE,
    DayNumber INT,
    MonthNumber INT,
    MonthName VARCHAR(20),
    QuarterNumber INT,
    YearNumber INT
);

-- Fact Table
CREATE TABLE FactSales
(
    SalesKey INT IDENTITY(1,1) PRIMARY KEY,

    DateKey INT,
    CustomerKey INT,
    ProductKey INT,
    PaymentKey INT,

    Quantity INT,
    Revenue DECIMAL(18,2),

    FOREIGN KEY (DateKey)
        REFERENCES DimDate(DateKey),

    FOREIGN KEY (CustomerKey)
        REFERENCES DimCustomer(CustomerKey),

    FOREIGN KEY (ProductKey)
        REFERENCES DimProduct(ProductKey),

    FOREIGN KEY (PaymentKey)
        REFERENCES DimPayment(PaymentKey)
);


SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
ORDER BY TABLE_NAME;


SELECT * 
FROM DimCustomer;

SELECT COUNT(*)
FROM DimCustomer;

SELECT *
FROM DimPayment;

SELECT MIN(OrderDate), MAX(OrderDate)
FROM RetailDWProject.dbo.Orders;

SELECT COUNT(*) AS DateCount
FROM DimDate;

SELECT COUNT(*) AS TotalDates
FROM DimDate;

SELECT COUNT(*) AS ProductCount
FROM DimProduct;

SELECT COUNT(*) AS CustomerCount
FROM DimCustomer;

SELECT COUNT(*) AS PaymentCount
FROM DimPayment;

SELECT COUNT(*) AS DateCount
FROM DimDate;

SELECT COUNT(*) AS ProductCount
FROM RetailDWProject.dbo.Products;

SELECT COUNT(*) AS ProductCount
FROM DimProduct;

SELECT COUNT(*) AS FactCount
FROM FactSales;


CREATE TABLE DimStore
(
    StoreKey INT IDENTITY(1,1) PRIMARY KEY,

    StoreID INT,
    StoreName VARCHAR(100),
    City VARCHAR(50),
    Region VARCHAR(50)
);

SELECT * FROM DimStore;

SELECT TOP 5 *
FROM FactSales;

ALTER TABLE FactSales
ADD
    StoreKey INT NULL,
    Cost DECIMAL(18,2) NULL,
    Profit DECIMAL(18,2) NULL,
    ProfitMargin DECIMAL(18,2) NULL;

SELECT TOP 5 *
FROM DimProduct;

ALTER TABLE DimProduct
ADD
    UnitPrice DECIMAL(18,2) NULL,
    CostPrice DECIMAL(18,2) NULL;

UPDATE dp
SET
    dp.UnitPrice = p.UnitPrice,
    dp.CostPrice = p.CostPrice
FROM RetailDW.dbo.DimProduct dp
INNER JOIN RetailDWProject.dbo.Products p
    ON dp.ProductID = p.ProductID;

SELECT TOP 5 *
FROM DimProduct;


UPDATE fs
SET fs.Cost = fs.Quantity * dp.CostPrice
FROM FactSales fs
INNER JOIN DimProduct dp
    ON fs.ProductKey = dp.ProductKey;

UPDATE FactSales
SET Profit = Revenue - Cost;

UPDATE FactSales
SET ProfitMargin =
    CASE
        WHEN Revenue = 0 THEN 0
        ELSE (Profit * 100.0) / Revenue
    END;


SELECT TOP 10
    Revenue,
    Cost,
    Profit,
    ProfitMargin
FROM FactSales;


SELECT TOP 10
    SalesKey,
    ProductKey,
    Revenue
FROM FactSales;

SELECT TOP 10
    OrderItemID,
    ProductID,
    LineTotal
FROM RetailDWProject.dbo.OrderItems;


Select * from dimstore;

SELECT
    COUNT(*) TotalRows,
    COUNT(StoreKey) FilledStoreKeys
FROM FactSales;

SELECT TOP 20
    SalesKey,
    StoreKey,
    Revenue
FROM FactSales;

UPDATE FactSales
SET StoreKey = ((SalesKey - 1) % 5) + 1;

SELECT TOP 20
    SalesKey,
    StoreKey
FROM FactSales;
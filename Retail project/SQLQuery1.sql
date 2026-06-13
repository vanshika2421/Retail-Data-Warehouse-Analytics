CREATE Database RetailDWProject;
Go 

USE RetailDWProject;
GO

CREATE TABLE Customers
(
CustomerID INT IDENTITY(1,1) PRIMARY KEY,
FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    Phone VARCHAR(20),
    City VARCHAR(50),
    State VARCHAR(50),
CreatedDate DATETIME DEFAULT GETDATE()
);

CREATE TABLE Products
(
    ProductID INT IDENTITY(1,1) PRIMARY KEY,
    ProductName VARCHAR(100) NOT NULL,
    Category VARCHAR(50),
    Brand VARCHAR(50),
    UnitPrice DECIMAL(10,2),
    CostPrice DECIMAL(10,2),
    CreatedDate DATETIME DEFAULT GETDATE()
);

CREATE TABLE Orders
(
    OrderID INT IDENTITY(1,1) PRIMARY KEY,
    CustomerID INT NOT NULL,
    OrderDate DATETIME DEFAULT GETDATE(),
    OrderStatus VARCHAR(20),
    TotalAmount DECIMAL(12,2),

    CONSTRAINT FK_Orders_Customers
    FOREIGN KEY (CustomerID)
    REFERENCES Customers(CustomerID)
);

CREATE TABLE OrderItems
(
    OrderItemID INT IDENTITY(1,1) PRIMARY KEY,
    OrderID INT NOT NULL,
    ProductID INT NOT NULL,
    Quantity INT NOT NULL,
    UnitPrice DECIMAL(10,2),
    LineTotal DECIMAL(12,2),

    CONSTRAINT FK_OrderItems_Orders
    FOREIGN KEY (OrderID)
    REFERENCES Orders(OrderID),

    CONSTRAINT FK_OrderItems_Products
    FOREIGN KEY (ProductID)
    REFERENCES Products(ProductID)
);


CREATE TABLE Payments
(
    PaymentID INT IDENTITY(1,1) PRIMARY KEY,
    OrderID INT NOT NULL,
    PaymentMethod VARCHAR(30),
    PaymentDate DATETIME DEFAULT GETDATE(),
    Amount DECIMAL(12,2),

    CONSTRAINT FK_Payments_Orders
    FOREIGN KEY (OrderID)
    REFERENCES Orders(OrderID)
);

CREATE TABLE Inventory
(
    InventoryID INT IDENTITY(1,1) PRIMARY KEY,
    ProductID INT NOT NULL,
    StockQuantity INT,
    ReorderLevel INT,
    LastUpdated DATETIME DEFAULT GETDATE(),

    CONSTRAINT FK_Inventory_Products
    FOREIGN KEY (ProductID)
    REFERENCES Products(ProductID)
);

SELECT SERVERPROPERTY('ServerName') AS ServerName;

SELECT @@SERVERNAME;

SELECT COUNT(*) AS TotalCustomers
FROM Customers;

SELECT TOP 10 *
FROM Customers;

SELECT COUNT(*) AS TotalProducts
FROM Products;

SELECT TOP 10 *
FROM Products;

SELECT COUNT(*) AS TotalInventory
FROM Inventory;

SELECT TOP 10 *
FROM Inventory;

SELECT COUNT(*) AS TotalOrders
FROM Orders;

SELECT TOP 10 *
FROM Orders;


SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE';


CREATE TABLE OrderItems
(
    OrderItemID INT IDENTITY(1,1) PRIMARY KEY,
    OrderID INT NOT NULL,
    ProductID INT NOT NULL,
    Quantity INT NOT NULL,
    UnitPrice DECIMAL(10,2),
    LineTotal DECIMAL(12,2),

    CONSTRAINT FK_OrderItems_Orders
    FOREIGN KEY (OrderID)
    REFERENCES Orders(OrderID),

    CONSTRAINT FK_OrderItems_Products
    FOREIGN KEY (ProductID)
    REFERENCES Products(ProductID)
);

SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE';

SELECT COUNT(*) AS TotalOrderItems
FROM OrderItems;


SELECT COUNT(*) AS TotalPayments
FROM Payments;

SELECT TOP 5
    p.ProductName,
    SUM(oi.LineTotal) AS TotalRevenue
FROM Products p
INNER JOIN OrderItems oi
    ON p.ProductID = oi.ProductID
GROUP BY p.ProductName
ORDER BY TotalRevenue DESC;


SELECT TOP 10
    c.CustomerID,
    c.FirstName,
    c.LastName,
    SUM(o.TotalAmount) AS TotalSpent
FROM Customers c
INNER JOIN Orders o
    ON c.CustomerID = o.CustomerID
GROUP BY
    c.CustomerID,
    c.FirstName,
    c.LastName
ORDER BY TotalSpent DESC;

/* Monthly Sales Trend */
SELECT
    YEAR(OrderDate) AS SalesYear,
    MONTH(OrderDate) AS SalesMonth,
    SUM(TotalAmount) AS Revenue
FROM Orders
GROUP BY
    YEAR(OrderDate),
    MONTH(OrderDate)
ORDER BY
    SalesYear,
    SalesMonth;

SELECT
    p.ProductName,
    i.StockQuantity,
    i.ReorderLevel
FROM Inventory i
INNER JOIN Products p
    ON i.ProductID = p.ProductID
WHERE i.StockQuantity < i.ReorderLevel;

SELECT
    p.ProductName,
    i.StockQuantity,
    i.ReorderLevel
FROM Inventory i
INNER JOIN Products p
    ON i.ProductID = p.ProductID;

    SELECT
    p.Category,
    p.ProductName,
    SUM(oi.LineTotal) AS Revenue
FROM Products p
INNER JOIN OrderItems oi
    ON p.ProductID = oi.ProductID
GROUP BY
    p.Category,
    p.ProductName;

WITH ProductRevenue AS
(
    SELECT
        p.Category,
        p.ProductName,
        SUM(oi.LineTotal) AS Revenue,

        ROW_NUMBER() OVER
        (
            PARTITION BY p.Category
            ORDER BY SUM(oi.LineTotal) DESC
        ) AS rn

    FROM Products p
    INNER JOIN OrderItems oi
        ON p.ProductID = oi.ProductID

    GROUP BY
        p.Category,
        p.ProductName
)

SELECT
    Category,
    ProductName,
    Revenue
FROM ProductRevenue
WHERE rn = 1;


CREATE TABLE Stores
(
    StoreID INT IDENTITY(1,1) PRIMARY KEY,
    StoreName VARCHAR(100),
    City VARCHAR(50),
    Region VARCHAR(50)
);

INSERT INTO Stores
(StoreName, City, Region)
VALUES
('Delhi Mega Store','Delhi','North'),
('Mumbai Central','Mumbai','West'),
('Bangalore Hub','Bangalore','South'),
('Chennai Plaza','Chennai','South'),
('Kolkata Mall','Kolkata','East');

SELECT * FROM Stores;

SELECT TOP 5 *
FROM Products;

SELECT TOP 5 *
FROM Orders;

SELECT TOP 5 *
FROM OrderItems;

ALTER TABLE Orders
ADD StoreID INT NULL;

UPDATE Orders
SET StoreID = ((OrderID - 1) % 5) + 1;

SELECT TOP 10
    OrderID,
    CustomerID,
    StoreID,
    OrderDate,
    TotalAmount
FROM Orders;

ALTER TABLE Orders
ADD CONSTRAINT FK_Orders_Stores
FOREIGN KEY (StoreID)
REFERENCES Stores
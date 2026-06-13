# 🏪 Retail Data Warehouse & Analytics Platform

> End-to-End Data Engineering & Business Intelligence Project using SQL Server, Python ETL, and Power BI.

![Power BI](https://img.shields.io/badge/PowerBI-Dashboard-yellow)
![SQL Server](https://img.shields.io/badge/SQL%20Server-Data%20Warehouse-red)
![Python](https://img.shields.io/badge/Python-ETL-blue)
![Star Schema](https://img.shields.io/badge/Data%20Model-Star%20Schema-green)

---

## 📌 Project Overview

Retail organizations generate large volumes of transactional data every day. However, operational databases are not optimized for business analytics.

This project demonstrates how raw retail transactions can be transformed into a scalable analytical platform using Data Warehousing principles, ETL pipelines, and interactive Power BI dashboards.

The solution enables stakeholders to analyze:

✅ Revenue Trends
✅ Product Performance
✅ Customer Behavior
✅ Payment Method Usage
✅ Regional Sales Performance
✅ Store Performance
✅ Profitability Metrics

---

## 🏗️ Solution Architecture

```text
OLTP Database
     │
     ▼
Python ETL Pipelines
     │
     ▼
Retail Data Warehouse
(Star Schema)
     │
     ▼
Power BI Dashboard
```

---

## 🗄️ Source System (OLTP)

### Transactional Tables

* Customers
* Products
* Orders
* OrderItems
* Payments
* Inventory
* Stores

---

## ⭐ Data Warehouse Design

### Fact Table

#### FactSales

| Column       |
| ------------ |
| SalesKey     |
| DateKey      |
| CustomerKey  |
| ProductKey   |
| PaymentKey   |
| StoreKey     |
| Quantity     |
| Revenue      |
| Cost         |
| Profit       |
| ProfitMargin |

---

### Dimension Tables

* DimCustomer
* DimProduct
* DimDate
* DimPayment
* DimStore

---

## 📊 Star Schema

```text
                DimDate
                   │
                   │
DimCustomer ─ FactSales ─ DimProduct
                   │
                   │
             DimPayment
                   │
                   │
              DimStore
```

---

## ⚙️ ETL Implementation

Python ETL scripts were developed using PyODBC to automate data movement from the OLTP database into the analytical warehouse.

### ETL Components

* etl_dim_customer.py
* etl_dim_date.py
* etl_dim_store.py
* etl_load_dimensions.py
* etl_fact_sales.py

### ETL Workflow

1. Extract transactional data
2. Load dimensions
3. Generate surrogate keys
4. Build FactSales
5. Calculate profitability metrics
6. Load Data Warehouse

---

## 🚀 Advanced Enhancements

### Store Analytics

Added:

* DimStore
* StoreKey relationships
* Revenue by Region
* Revenue by Store

### Profitability Analytics

Implemented:

* Cost Calculation
* Profit Calculation
* Profit Margin %

Formula:

Profit = Revenue − Cost

Profit Margin % = (Profit / Revenue) × 100

---

## 📈 Power BI Dashboard

### KPI Metrics

* Total Revenue
* Total Profit
* Profit Margin %
* Total Orders

### Visualizations

📊 Revenue by Category

📊 Revenue by Product

📊 Revenue by Region

🥧 Revenue by Payment Method

📈 Monthly Revenue Trend

🎯 Category Filters

---

## 📷 Dashboard Preview

### Main Dashboard

(Add Screenshot Here)

### Region Analysis

(Add Screenshot Here)

---

## 🛠️ Technologies Used

| Category        | Technology  |
| --------------- | ----------- |
| Database        | SQL Server  |
| ETL             | Python      |
| Connectivity    | PyODBC      |
| Data Modeling   | Star Schema |
| BI Tool         | Power BI    |
| Version Control | GitHub      |

---

## 📁 Project Structure

```text
Retail-Data-Warehouse-Analytics
│
├── SQL
├── ETL
├── PowerBI
├── Screenshots
├── README.md
└── requirements.txt
```

---

## 🎯 Business Insights Generated

* Top Performing Products
* Revenue Contribution by Category
* Regional Revenue Distribution
* Store-Level Performance Analysis
* Monthly Revenue Trends
* Payment Method Analysis
* Profitability Tracking

---

## 💼 Resume Highlights

* Designed and implemented a Retail Data Warehouse using Star Schema architecture.
* Developed Python ETL pipelines for loading dimension and fact tables.
* Built analytical KPIs including Revenue, Profit, Profit Margin, and Regional Performance.
* Created interactive Power BI dashboards for executive-level reporting.
* Implemented dimensional modeling and business intelligence reporting workflows.
* Delivered an end-to-end analytics platform integrating SQL Server, Python, and Power BI.

---

## 👩‍💻 Author

**Vanshika Kamra**

Data Analyst | SQL Developer | Power BI Developer | Data Engineering Enthusiast

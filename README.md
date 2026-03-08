# Inventory Reconciliation & Sales Analysis Engine (Python)

## Project Overview

This project implements an **Inventory Reconciliation and Sales Analysis Engine** for an e-commerce company.
The system processes inventory and sales transaction data, applies business rules, reconciles stock levels, and generates analytical reports and dashboards.

The application ensures **data validation, safe processing of invalid records, and automated reporting**, enabling operations teams to identify stock issues and understand product sales performance.

The system is built using **Python**, with modular components for data ingestion, aggregation, business logic, reporting, logging, and visualization.

---

# Project Structure

```
inventory_project/
│
├── data/
│   ├── inventory.csv
│   └── sales_transactions.csv
│
├── src/
│   ├── loader.py
│   ├── sales_aggregator.py
│   ├── inventory_engine.py
│   ├── reporter.py
│   ├── dashboard.py
│   ├── config_loader.py
│   └── main.py
│
├── tests/
│   ├── test_sales_aggregator.py
│   └── test_inventory_engine.py
│
├── logs/
│   └── inventory.log
│
├── inventory_reconciliation.csv
├── category_summary.csv
├── data_quality_report.json
├── sales_dashboard.html
└── README.md
```

---

# Key Features

### Data Processing

* Reads inventory data from CSV files
* Reads sales transaction records
* Aggregates sales per product

### Inventory Reconciliation

* Calculates final stock after sales
* Prevents negative stock values
* Detects stock errors

### Stock Status Classification

Products are classified into:

* **AVAILABLE** → stock greater than 10
* **LOW_STOCK** → stock between 1 and 10
* **OUT_OF_STOCK** → stock equals 0
* **STOCK_ERROR** → sales exceed inventory

### Data Validation

The system safely handles invalid data:

* Invalid transaction dates are ignored
* Negative sales quantities are ignored
* Unknown product IDs are logged
* Processing continues without application crashes

### Logging

All data issues are logged into:

```
logs/inventory.log
```

Example log entries:

```
WARNING - Invalid date skipped
WARNING - Unknown product id
WARNING - Negative quantity ignored
```

### Reporting

The system generates multiple output reports:

**1. Inventory Reconciliation Report**

`inventory_reconciliation.csv`

Contains:

```
product_id
product_name
category
current_stock
total_sold_quantity
final_stock
stock_status
total_sales_value
```

**2. Category Sales Summary**

`category_summary.csv`

Shows total sales value by product category.

**3. Data Quality Report**

`data_quality_report.json`

Contains metrics:

```
invalid_dates
negative_quantities
unknown_products
valid_transactions
```

### Analytics Dashboard

The project generates an **interactive dashboard** using Plotly:

```
sales_dashboard.html
```

Dashboard includes:

* Sales by category (bar chart)
* Stock status distribution (donut chart)
* Top selling products (bar chart)

The dashboard is interactive and can be viewed in any web browser.

---

# Business Rules

### Sales Filtering

Only transactions for **April 2024** are considered.

Transactions are ignored if:

* Date format is invalid
* Quantity is negative
* Product ID does not exist in inventory

### Sales Aggregation

Sales are aggregated per product:

```
total_quantity_sold = sum(quantity_sold)
```

### Inventory Reconciliation

```
final_stock = current_stock - total_quantity_sold
```

If:

```
final_stock < 0 → final_stock = 0
stock_status = STOCK_ERROR
```

### Sales Value Calculation

```
total_sales_value = total_sold_quantity * unit_price
```

---

# Installation

### 1. Clone or Download Project

```
git clone <repository-url>
cd inventory_project
```

### 2. Install Required Libraries

```
pip install plotly
```

---

# Running the Application

Run the system from the project root:

```
python src/main.py
```

Example output:

```
Starting Inventory Processing Engine

Processing completed successfully!
Processed Period: 4/2024
Valid Transactions Processed: 30
Execution Time: 0.45 seconds
```

---

# Running Unit Tests

To run all tests:

```
python -m unittest discover tests -v
```

Example output:

```
Ran 13 tests in 0.009s

OK
```

Tests cover:

* Sales aggregation logic
* Inventory calculations
* Edge cases and error handling

---

# Example Dashboard Output

The generated dashboard displays:

* Total sales by product category
* Distribution of stock availability
* Top 5 selling products

Open the dashboard:

```
sales_dashboard.html
```

---

# Assumptions

* Inventory data contains valid product definitions.
* Sales transactions may contain invalid records which are safely ignored.
* Only **April 2024 transactions** are included in calculations.

---

# Edge Cases Handled

The system safely handles:

* Missing product IDs
* Invalid date formats
* Negative quantities
* Unknown products
* Excess sales beyond available stock

---

# Technologies Used

* Python
* CSV processing
* JSON reporting
* Logging module
* Plotly visualization
* Unit testing (unittest)

---

# Future Improvements

Possible enhancements:

* Database integration (PostgreSQL / MySQL)
* Real-time data pipeline
* Web dashboard using Streamlit
* REST API for inventory services
* Scheduled processing pipeline

---

# Conclusion

This project demonstrates how to build a **modular data processing and analytics system** that performs inventory reconciliation, handles invalid data safely, and produces analytical insights through reports and dashboards.

It reflects real-world practices used in **data engineering and backend analytics systems**.

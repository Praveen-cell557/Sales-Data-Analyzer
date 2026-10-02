# 📊 Sales Data Analyzer

A practical **Data Science project** built with **Python, Pandas, and NumPy** to analyze a real-world sales dataset and extract meaningful business insights.

The project performs **data exploration, data quality checking, statistical analysis, product analysis, category analysis, regional analysis, and performance analysis**.

The goal is to understand how raw sales data can be processed and converted into useful information for analysis and decision-making.

---

## 🚀 Project Overview

The **Sales Data Analyzer** analyzes a sales dataset containing information about:

* Orders
* Customers
* Products
* Categories
* Sub-Categories
* Regions
* Sales
* Order dates
* Shipping information

The project uses **Pandas** for data manipulation and **NumPy** for numerical and statistical calculations.

---

## 🔍 What This Project Analyzes

### 1. Dataset Overview

The project displays:

* First 5 records
* Last 5 records
* Number of rows
* Number of columns
* Available column names

This helps understand the structure and contents of the dataset before performing analysis.

### 2. Data Quality Analysis

The project checks:

* Missing values
* Duplicate records

This provides basic data-cleaning and validation experience.

### 3. Sales Statistics

The project calculates:

* Total Sales
* Average Sale
* Highest Sale
* Lowest Sale
* Median Sale
* Standard Deviation

These statistics provide an overview of the distribution and behavior of sales.

### 4. Top 5 Sales Analysis

The project identifies the five largest individual sales transactions and displays:

* Product Name
* Category
* Sales Amount

### 5. Above-Average Sales Analysis

The project identifies transactions where the sales value is greater than the overall average sales value.

This demonstrates conditional filtering using Pandas.

### 6. Category-Wise Sales Analysis

Sales are grouped by category, such as:

* Furniture
* Office Supplies
* Technology

The project calculates total sales for each category and identifies the category with the highest total sales.

### 7. Region-Wise Sales Analysis

Sales are grouped by region:

* Central
* East
* South
* West

The project calculates total sales for each region and identifies the region with the highest total sales.

### 8. Sub-Category Analysis

The project calculates total sales for each product sub-category and identifies the highest-performing sub-category.

### 9. Product Analysis

The project calculates:

* Unique Products
* Unique Customers
* Unique Orders

This helps understand the overall scale of the dataset.

### 10. Most Common Category

The project identifies the category that appears most frequently in the dataset using the mode.

The most common category is not necessarily the category with the highest sales.

### 11. Most Common Region

The project identifies the region that appears most frequently in the dataset.

This is different from identifying the region with the highest total sales.

### 12. Average Sales by Category

The project calculates the average transaction value for each category.

This provides another way to compare category performance.

### 13. Highest-Sale Product

The project identifies the product associated with the highest individual sales transaction.

### 14. Final Business Summary

The program generates a final summary containing:

* Total Records
* Total Sales
* Average Sale
* Total Orders
* Total Customers
* Total Products
* Best Category
* Best Region
* Best Sub-Category
* Most Common Category
* Most Common Region
* Highest Sale

---

## 🧠 Pandas Concepts Used

| Pandas Function | Purpose                         |
| --------------- | ------------------------------- |
| `pd.read_csv()` | Load CSV data                   |
| `head()`        | View first records              |
| `tail()`        | View last records               |
| `shape`         | Get dataset dimensions          |
| `columns`       | View column names               |
| `isnull()`      | Check missing values            |
| `duplicated()`  | Check duplicate rows            |
| `sort_values()` | Sort data                       |
| `groupby()`     | Group data                      |
| `sum()`         | Calculate totals                |
| `mean()`        | Calculate averages              |
| `nunique()`     | Count unique values             |
| `mode()`        | Find most common value          |
| `idxmax()`      | Find maximum-value index        |
| `loc[]`         | Select specific records         |
| Filtering       | Select records using conditions |

---

## 🔢 NumPy Concepts Used

| NumPy Function | Purpose                      |
| -------------- | ---------------------------- |
| `np.sum()`     | Calculate total              |
| `np.mean()`    | Calculate average            |
| `np.max()`     | Find maximum                 |
| `np.min()`     | Find minimum                 |
| `np.median()`  | Find median                  |
| `np.std()`     | Calculate standard deviation |

---

## 📊 Example Results

The included dataset contains **9,800 records**.

```text
Total Records       : 9800
Total Sales         : 2261536.78
Average Sale        : 230.77
Highest Sale        : 22638.48
Lowest Sale         : 0.44
Median Sale         : 54.49
Standard Deviation  : 626.62

Unique Products     : 1861
Unique Customers    : 793
Unique Orders       : 4922
```

### Category Sales

```text
Furniture           : 728658.58
Office Supplies     : 705422.33
Technology          : 827455.87
```

### Regional Sales

```text
Central             : 492646.91
East                : 669518.73
South               : 389151.46
West                : 710219.68
```

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **CSV Dataset**

No external APIs or paid services are required.

---

## 📁 Project Structure

```text
sales-data-analyzer/
│
├── python.py
├── sales.csv
├── README.md
├── .gitignore
└── LICENSE
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project

```bash
cd sales-data-analyzer
```

### 3. Install dependencies

```bash
pip install pandas numpy
```

### 4. Run the analyzer

```bash
python python.py
```

The program will load the included `sales.csv` file and display the complete analysis in the terminal.

---

## 🎯 Learning Objectives

This project demonstrates practical understanding of:

* Python for Data Science
* Pandas
* NumPy
* CSV data handling
* Data exploration
* Data quality checking
* Statistical analysis
* Data filtering
* Data sorting
* Data grouping
* Aggregation
* Business-oriented data analysis
* Extracting insights from real-world data

---

## 🔄 Data Analysis Workflow

```text
Sales Dataset
      ↓
Load Data
      ↓
Explore Dataset
      ↓
Check Data Quality
      ↓
Calculate Statistics
      ↓
Analyze Sales
      ↓
Analyze Categories
      ↓
Analyze Regions
      ↓
Analyze Sub-Categories
      ↓
Analyze Products
      ↓
Extract Insights
      ↓
Generate Final Summary
```

---

## 🔮 Future Improvements

* Monthly sales analysis
* Year-wise sales analysis
* Sales trend analysis
* Date-based analysis
* Customer segmentation
* Product performance ranking
* Matplotlib visualizations
* Interactive charts
* Streamlit dashboard
* Automated business reports

---

## 👨‍💻 Author

**Praveen Rathod (Radheya Karn)**

CSE Student | Cybersecurity Enthusiast | Python & Data Science Learner

---

## 📄 License

This project is licensed under the **MIT License**.

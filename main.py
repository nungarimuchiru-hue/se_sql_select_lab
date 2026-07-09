# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")


# STEP 2
# First five employees
df_first_five = pd.read_sql("""
SELECT *
FROM employees
LIMIT 5;
""", conn)

# STEP 3
# Five employees in reverse order
df_five_reverse = pd.read_sql("""
SELECT *
FROM employees
ORDER BY EmployeeId DESC
LIMIT 5;
""", conn)

# STEP 4
# Aliasing columns
df_alias = pd.read_sql("""
SELECT
    FirstName AS First_Name,
    LastName AS Last_Name,
    Title AS Job_Title
FROM employees;
""", conn)

# STEP 5
# CASE statement
df_executive = pd.read_sql("""
SELECT
    FirstName,
    LastName,
    Title,
    CASE
        WHEN Title LIKE '%Manager%' THEN 'Executive'
        ELSE 'Staff'
    END AS Employee_Type
FROM employees;
""", conn)

# STEP 6
# String function
df_name_length = pd.read_sql("""
SELECT
    FirstName,
    LENGTH(FirstName) AS Name_Length
FROM employees;
""", conn)

# STEP 7
# Short title using SUBSTR
df_short_title = pd.read_sql("""
SELECT
    Title,
    SUBSTR(Title, 1, 10) AS Short_Title
FROM employees;
""", conn)

# STEP 8
# Numeric function
sum_total_price = pd.read_sql("""
SELECT
    SUM(UnitPrice) AS Total_Price
FROM products;
""", conn)

# STEP 9
# Date formatting
df_day_month_year = pd.read_sql("""
SELECT
    BirthDate,
    strftime('%d-%m-%Y', BirthDate) AS Day_Month_Year
FROM employees;
""", conn)
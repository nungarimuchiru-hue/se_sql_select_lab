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
# Five employees in reverse order (Adjust columns based on your prompt, e.g., employeeNumber and lastName)
df_five_reverse = pd.read_sql("""
SELECT employeeNumber, lastName
FROM employees
ORDER BY employeeNumber DESC;
""", conn)


# STEP 4
# Aliasing columns
df_alias = pd.read_sql("""
SELECT
    employeeNumber AS ID,
    firstName AS first_name,
    lastName AS last_name,
    jobTitle AS job_title
FROM employees;
""", conn)


# STEP 5
# CASE statement
df_executive = pd.read_sql("""
SELECT
    firstName,
    lastName,
    jobTitle,
    CASE
        WHEN jobTitle LIKE '%Manager%' THEN 'Executive'
        ELSE 'Staff'
    END AS role
FROM employees;
""", conn)

# STEP 6
# String function
df_name_length = pd.read_sql("""
SELECT
    firstName,
    LENGTH(firstName) AS name_length
FROM employees;
""", conn)

# STEP 7
# Short title using SUBSTR
df_short_title = pd.read_sql("""
SELECT
    jobTitle,
    SUBSTR(jobTitle, 1, 10) AS short_title
FROM employees;
""", conn)


# STEP 8
# Numeric function
sum_total_price = pd.read_sql("""
SELECT
    SUM(buyPrice) AS total_price
FROM products;
""", conn)


# STEP 9
# Date formatting
df_day_month_year = pd.read_sql("""
SELECT
    BirthDate,
    strftime('%d', BirthDate) AS day,
    strftime('%m', BirthDate) AS month,
    strftime('%Y', BirthDate) AS year
FROM employees;
""", conn)
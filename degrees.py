import pandas as pd
import sqlite3

conn = sqlite3.connect('database.db')
df = pd.read_csv('salaries-by-college-type.csv')
df.to_sql('collegetype', conn, if_exists='replace', index=False)

conn.close()

# Connect to SQLite database
with sqlite3.connect('database.db') as conn:
    # Read another CSV file into a DataFrame
    df = pd.read_csv('salaries-by-region.csv')
    # Write DataFrame to a different table in the SQLite database
    df.to_sql('collegeregion', conn, if_exists='replace', index=False)

# Connect to SQLite database
with sqlite3.connect('database.db') as conn:
    # Read another CSV file into a DataFrame
    df = pd.read_csv('degrees-that-pay-back.csv')
    # Write DataFrame to a different table in the SQLite database
    df.to_sql('collegemajor', conn, if_exists='replace', index=False)

 ORDER BY CAST("Mid-Career Median Salary" AS REAL) ASC; -- for decimal numbers

SELECT "Undergraduate Major", "Starting Median Salary", "Mid-Career Median Salary"
FROM collegemajor
ORDER BY CAST(REPLACE("Starting Median Salary", '$', '') AS REAL) DESC
LIMIT 5;

SELECT "School Name", "Starting Median Salary", "Mid-Career Median Salary"
FROM collegetype
ORDER BY CAST(REPLACE("Mid-Career Median Salary", '$', '') AS REAL) DESC
LIMIT 5;
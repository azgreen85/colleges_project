import sqlite3
import pandas as pd

def export_query_to_csv(query, database, output_csv):
    # Connect to SQLite database
    conn = sqlite3.connect(database)
    
    # Execute the query and fetch the result into a DataFrame
    df = pd.read_sql_query(query, conn)
    
    # Export DataFrame to CSV
    df.to_csv(output_csv, index=False)
    
    # Close the connection
    conn.close()

# Define the SQL queries
queries = {
    'top_5_starting_salaries.csv': '''
        SELECT "Undergraduate Major", "Starting Median Salary", "Mid-Career Median Salary"
        FROM collegemajor
        ORDER BY CAST(REPLACE(REPLACE("Starting Median Salary", '$', ''), ',', '') AS REAL) DESC
        LIMIT 5;
    ''',
    'bottom_5_starting_salaries.csv': '''
        SELECT "Undergraduate Major", "Starting Median Salary", "Mid-Career Median Salary"
        FROM collegemajor
        ORDER BY CAST(REPLACE(REPLACE("Starting Median Salary", '$', ''), ',', '') AS REAL) ASC
        LIMIT 5;
    ''',
    'total_majors.csv': '''
        SELECT COUNT(*) AS "Total Majors"
        FROM collegemajor;
    ''',
    'top_5_mid_career_salaries.csv': '''
        SELECT "Undergraduate Major", "Starting Median Salary", "Mid-Career Median Salary"
        FROM collegemajor
        ORDER BY CAST(REPLACE(REPLACE("Mid-Career Median Salary", '$', ''), ',', '') AS REAL) DESC
        LIMIT 5;
    ''',
    'top_5_schools_starting_salaries.csv': '''
        SELECT "School Name", "Starting Median Salary"
        FROM collegeregion
        ORDER BY CAST(REPLACE(REPLACE("Starting Median Salary", '$', ''), ',', '') AS REAL) DESC
        LIMIT 5;
    ''',
    'top_5_schools_mid_career_salaries.csv': '''
        SELECT "School Name", "Mid-Career Median Salary"
        FROM collegeregion
        ORDER BY CAST(REPLACE(REPLACE("Mid-Career Median Salary", '$', ''), ',', '') AS REAL) DESC
        LIMIT 5;
    '''
    }

# Define database name
database_name = 'database.db'

# Export each query result to CSV
for output_csv, query in queries.items():
    export_query_to_csv(query, database_name, output_csv)

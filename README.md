# College Salaries Dashboard Project

## Project Overview

The goal of this project was to create a dashboard or a collection of visuals summarizing which majors, schools, and types of schools produce alumni with the highest earnings. This project involved several steps, including loading CSV files into a relational SQL database, writing SQL queries to retrieve the desired data, and visualizing the data using Tableau.

## Project Steps

1. **Loading CSV Files into SQL Database**:
   - The project starts with three CSV files containing data on college salaries:
     - `salaries-by-college-type.csv`
     - `degrees-that-pay-back.csv`
     - `salaries-by-region.csv`
   - These CSV files were loaded into a single relational SQL database using SQLite.

2. **SQL Queries**:
   - SQL queries were crafted to extract the data needed for the visualizations. 
   - The queries were written to select the top 5 and bottom 5 majors for starting and mid-career salaries, organized by school type, school name, and major.
   - The Python script `export_collegemajor_queries_to_csv.py` contains the SQL queries used to extract the data.

3. **Data Extraction**:
   - A Python program was scripted to load the CSV files into the database, run the SQL queries, and export the results back to CSV files.

4. **Data Visualization**:
   - The extracted data was visualized using Tableau to create an interactive dashboard.
   - The dashboard includes visuals for:
     - Top 5 majors by starting and mid-career salaries.
     - Top 5 schools by starting and mid-career salaries.
     - Top 5 school types by starting and mid-career salaries.
     - Bottom 5 majors for starting salaries in a visualization named "Majors to Avoid".
   - You can view the Tableau dashboard [here](https://public.tableau.com/views/DEgreees/Dashboard1?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link).

## Files Included

- `export_collegemajor_queries_to_csv.py`: Python script containing the SQL queries and code to export the data to CSV files.
- CSV Files:
  - `salaries-by-college-type.csv`
  - `degrees-that-pay-back.csv`
  - `salaries-by-region.csv`
- `database.db`: SQLite database containing the loaded data (optional, if you want to include the database file).
- `README.md`: This file.

## How to Run the Project

1. Ensure you have Python and SQLite installed on your machine.
2. Place the CSV files in the same directory as the `export_collegemajor_queries_to_csv.py` script.
3. Run the Python script to load the data into the database and export the queried data as CSV files:
   ```sh
   python3 export_collegemajor_queries_to_csv.py


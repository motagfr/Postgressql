# PostgreSQL Overview

This folder contains a small collection of example SQL scripts, Python notebooks, and helper scripts used for exploring and analyzing a PostgreSQL sample database (dvdrental). The content is educational and aimed at demonstrating how to connect to PostgreSQL, run queries, and visualize results with Python.

## What's in this folder

- `dvdrental_analysis.ipynb` - Jupyter notebook with exploratory analysis of the `dvdrental` sample database using SQL and Python (Pandas/Matplotlib). Contains query examples and charts.
- `First Connection.session.sql` - SQL session file capturing the commands used to establish a first connection or set up environment. Typically includes connection strings or initial setup queries.
- `select test.sql` - Small SQL script used to test basic SELECT queries against the database.
- `Untitled-1.sql` - An extra SQL file that may contain ad-hoc queries or experiments.

### `pg_charts/`

- `plot_monthly_sales.py` - Python script that connects to PostgreSQL, runs a query for monthly sales, and produces charts. Requires packages listed in `pg_charts/requirements.txt`.

- `requirements.txt` - Python dependencies needed for `plot_monthly_sales.py` (e.g., psycopg2, pandas, matplotlib).

### `SQL-in-Python/`

- `dvdrental_analysis.ipynb` - Another copy or variant of the analysis notebook, showing how to embed SQL queries in Python workflows.

## Purpose

The repository is intended as an instructional workspace to:

- Demonstrate connecting to a PostgreSQL database from both SQL clients and Python.
- Provide example queries and analysis workflows for the `dvdrental` sample database.
- Show basic visualizations of query results using Python.

## Quick start

1. Install PostgreSQL and import the `dvdrental` sample database if you don't already have it. The sample DB is available from PostgreSQL documentation and mirrors.
2. If running Python scripts or notebooks, create a virtual environment and install dependencies. From the `pg_charts` directory, run:

   python -m venv .venv
   .\.venv\Scripts\activate
   pip install -r pg_charts\requirements.txt

3. Update connection parameters in the notebooks or scripts to match your local PostgreSQL credentials (host, port, user, password, dbname).

## Notes and tips

- Keep credentials out of source control. Use environment variables or a local configuration file excluded from version control.
- The notebooks are ideal for learning; run them step-by-step and inspect the SQL queries.

## License

This is an educational collection. If you copy or redistribute code, include an appropriate license or attribution.

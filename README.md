# SQL Quest
A Python project for executing SQL queries against various data sources.

## Features
* Execute SQL queries against Snowflake, BigQuery, and Redshift
* Log query executions with query ID, user ID, data source, and timestamp
* Handle errors from the data warehouse and display the original SQL error message

## Usage
1. Create an instance of the `SQLQuest` class
2. Call the `execute_query` method with the query ID, user ID, data source, and query
3. Get the query log using the `get_query_log` method

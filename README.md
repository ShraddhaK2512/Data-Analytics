# Crime Analysis in Phoenix, Arizona
Utilizing Databricks Public Version & Real-Time API

# Project Overview
This project analyzes crime patterns in Phoenix, Arizona using real-time crime data from an API. 
It processes data using Apache Spark (PySpark) in Databricks and visualizes insights with Seaborn & Matplotlib.

## Tech Stacks and Libraries
- Databricks (Public Version)
- Python
- Apache Spark (PySpark)
  `from pyspark.sql import SparkSession`
  `from pyspark.sql.functions import col, count, year, to_timestamp`
- Data Handling & APIs
  `import requests`
  `import pandas as pd`
- Data Visualization
  `import matplotlib.pyplot as plt`

## Project Workflow
  1 Create a Spark Session: 
    `spark = SparkSession.builder.appName("CrimeAnalysis").getOrCreate()`
  2 Fetch Data from Real-Time API
      Uses requests to fetch JSON data.
  3 Convert JSON Data to Pandas DataFrame
      `df = pd.DataFrame(response.json())`
  4 Convert Pandas DataFrame to Spark DataFrame
      `spark_df = spark.createDataFrame(df)`

## Key Questions Answered
  1 What are the most prevalent crime types in Phoenix?
  2 Where are the crime hotspots in Phoenix?
  3 What are the temporal patterns of crime in Phoenix?

  Finally Converted Spark DataFrame to Pandas DataFrame for visualization.

  ## Project Notebook Link
  [Crime Analysis Project Databricks Notebook]: https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/4819981603588590/249422360864141/6315475593687325/latest.html

  ## Open Data link source
  [Data Source]: https://www.phoenixopendata.com/dataset/crime-data

  ## How to Run the Project
  - Load the Databricks notebook.
  - Run the API request to fetch real-time data.
  - Execute data transformation & analysis steps.
  - Visualize crime patterns.


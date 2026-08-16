# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC # Data Visualization
# MAGIC
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) In this lesson you:
# MAGIC Explore data visualization of **`pandas`** DataFrames using:
# MAGIC - Databricks built-in plotting
# MAGIC - **`pandas`** plotting methods
# MAGIC - **`seaborn`** plotting functionality
# MAGIC
# MAGIC Let's import **`pandas`** and our Airbnb Dataset

# COMMAND ----------

# MAGIC %run "./Includes/Classroom-Setup"

# COMMAND ----------

import pandas as pd

# COMMAND ----------

file_path = f"{DA.paths.datasets}/sf-airbnb/sf-airbnb.csv".replace("dbfs:", "/dbfs")
df = pd.read_csv(file_path)
df.head(3)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Built-in Plotting
# MAGIC
# MAGIC Databricks provides built in data visualization tools we can use in a Databricks notebook. 
# MAGIC
# MAGIC In order to use them, we use the built-in **`display()`** function Databricks provides on a pandas DataFrame.
# MAGIC
# MAGIC By default, we just see the `DataFrame` as a table. However, if you click the bottom middle bar chart icon we can switch to plotting mode.

# COMMAND ----------

display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Plot Options
# MAGIC
# MAGIC In order to change the kind of plot we see we can click "Plot Options" next to the bar chart icon.
# MAGIC
# MAGIC From there we can specify what kind of plot we want on which columns of the DataFrame.
# MAGIC
# MAGIC For example, let's say we wanted to view the average number of bedrooms per neighborhood. 
# MAGIC
# MAGIC To do this:
# MAGIC
# MAGIC 1. Click Plot Options.
# MAGIC 2. Add **`neighborhood`** to the keys.
# MAGIC 3. Add **`bedrooms`** to the values.
# MAGIC 3. Change the aggregate function to average.
# MAGIC 4. Make sure we have a bar chart selected.

# COMMAND ----------

display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC Note that initially it only will show a preview of the first 1000 rows, but when we click **`apply`** it works on all of them.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Pandas Plotting
# MAGIC
# MAGIC **`pandas`** also provides some plotting functionality. 
# MAGIC
# MAGIC We can create a histogram using the **`hist()`** method on a **`Series`**.
# MAGIC
# MAGIC Let's create a histogram of the number of bedrooms:

# COMMAND ----------

df["bedrooms"].hist(bins=20)

# COMMAND ----------

# MAGIC %md
# MAGIC We can also specify the number of bins by passing an argument to **`bins`** parameter.

# COMMAND ----------

df["bedrooms"].hist(bins=20)

# COMMAND ----------

# MAGIC %md
# MAGIC We can also create box plots with pandas.
# MAGIC
# MAGIC We use the method **`boxplot([cols])`** on a **`DataFrame`** to create a box plot for each of the specified columns:

# COMMAND ----------

df.boxplot(["bedrooms", "bathrooms"])

# COMMAND ----------

# MAGIC %md
# MAGIC # Seaborn
# MAGIC
# MAGIC [seaborn](https://seaborn.pydata.org/) is a very popular data visualization library that works with pandas DataFrames. 
# MAGIC
# MAGIC It is popular for both being relatively easy to use and for producing nice looking visualizations.
# MAGIC
# MAGIC Let's import **`seaborn`**: it is common practice to use **`sns`** as the alias.

# COMMAND ----------

import seaborn as sns

# COMMAND ----------

# MAGIC %md
# MAGIC ## Scatter plot
# MAGIC
# MAGIC Let's first create a scatter plot. We'll plot **`bedrooms`** cases on the x-axis and **`bathrooms`** on the y-axis. 
# MAGIC
# MAGIC In order to do this, we call **`sns.scatterplot(data=, x=, y=)`**
# MAGIC
# MAGIC We provide a **`DataFrame`** as the data parameter, and the column names we want for the x and y parameters.

# COMMAND ----------

sns.scatterplot(data=df, x="bedrooms", y="bathrooms")

# COMMAND ----------

# MAGIC %md
# MAGIC You might also want to plot a line of best fit for the scatter plot. 
# MAGIC
# MAGIC We can do this by using the same parameters but for the **`regplot()`** function:

# COMMAND ----------

sns.regplot(data=df, x="bedrooms", y="bathrooms")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC &copy; 2025 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the 
# MAGIC <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/><a href="https://databricks.com/privacy-policy">Privacy Policy</a> | 
# MAGIC <a href="https://databricks.com/terms-of-use">Terms of Use</a> | 
# MAGIC <a href="https://help.databricks.com/">Support</a>
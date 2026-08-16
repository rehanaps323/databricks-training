# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC # Collection Types and Methods Lab
# MAGIC
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) In this lab you:<br>
# MAGIC
# MAGIC Apply concepts learned in the last lesson, including:
# MAGIC - Using objects and methods with new collection data types

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC #### Problem 1a: Dinner Foods
# MAGIC
# MAGIC We provide a list called **`dinner_list`** with elements "potatoes, peppers, onions" in that order.

# COMMAND ----------

dinner_list = ["sweet potatoes","peppers","onions"]
print(dinner_list)  


# COMMAND ----------

# MAGIC %md
# MAGIC #### Problem 1b: Dinner Foods 
# MAGIC
# MAGIC However, we actually ate sweet potatoes, not normal potatoes, so change the first element of the list to be "sweet potatoes".

# COMMAND ----------

assert dinner_list == ['sweet potatoes', 'peppers', 'onions'], "dinner_list should be ['sweet potatoes', 'peppers', 'onions']"
print("Test passed!")

# COMMAND ----------

# MAGIC %md
# MAGIC #### Problem 1c: Dinner Foods 
# MAGIC Finally, we also ate some rice, so add "rice" to the end of the list.

# COMMAND ----------

dinner_list= ["sweet potatoes", "peppers", "onions", "rice"]
print(dinner_list)

# COMMAND ----------

assert dinner_list == ['sweet potatoes', 'peppers', 'onions', 'rice'], "dinner_list should be ['sweet potatoes', 'peppers', 'onions', 'rice']"
print("Test passed!")

# COMMAND ----------

# MAGIC %md
# MAGIC #### Problem 2a: Dinner Dictionaries
# MAGIC
# MAGIC Create a dictionary called **`dinner_dict`** with pairs `"sweet potatoes": 3`, `"peppers": 4`, `"onions": 1` representing what we ate for dinner.

# COMMAND ----------

dinner_dict = {"sweet potatoes": 3, "peppers": 4, "onions": 1}
print(dinner_dict)

# COMMAND ----------

assert dinner_dict["sweet potatoes"] == 3, "We had 3 sweet potatoes"
assert dinner_dict["peppers"] == 4, "We had 4 peppers"
assert dinner_dict["onions"] == 1, "We had 1 onion"
print("Tests passed!")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC #### Problem 2b: Updating Dinner Dictionary
# MAGIC
# MAGIC After thinking about it, we realize we actually only had 2 `sweet potatoes`. And while we didn't want to admit it, we also had one `ice cream` as well.
# MAGIC
# MAGIC Update the dictionary to reflect those changes.

# COMMAND ----------

dinner_dict = {"sweet potatoes": 2, "ice cream": 1}
print(dinner_dict)

# COMMAND ----------

# MAGIC %md
# MAGIC **Check your work:**

# COMMAND ----------

assert dinner_dict["sweet potatoes"] == 2, "We had 2 sweet potatoes"
assert dinner_dict["ice cream"] == 1, "We had 1 ice cream (but don't tell!)"
print("Tests passed!")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Problem 3: Sets
# MAGIC
# MAGIC A very valuable skill for a programmer to have is to be able to look at documentation for a data type they do not know and understand how to use it. 
# MAGIC
# MAGIC With that in mind this exercise asks you to explore a new collection data type called **Sets**. 
# MAGIC
# MAGIC Use the documentation provided <a href="https://docs.python.org/3/tutorial/datastructures.html#sets" target="_blank">here</a> to complete the next problem.
# MAGIC
# MAGIC Create the following sets:
# MAGIC   * **`ingredient_set_1`** with the ingredients "carrots", "onions", and "potatoes".
# MAGIC   * **`ingredient_set_2`** with the ingredients "broccoli", "carrots", and "rice".
# MAGIC   * **`ingredient_set_3`** with the ingredients "sweet potatoes", "carrots", and "corn".
# MAGIC
# MAGIC Programmatically create a new set **`ingredient_intersection_set`** which contains only those ingredients that occur in all three sets.

# COMMAND ----------

ingredient_set_1= {"carrots", "potatoes", "broccoli"}
ingredient_set_2= {"rice", "broccoli", "carrots"}
ingredient_set_3 = {"sweet potatoes", "carrots", "corn"}
ingredient_intersection_set =   ingredient_set_1.intersection(ingredient_set_2, ingredient_set_3)
print(ingredient_intersection_set)

# COMMAND ----------

ingredient_set_1 = TODO
ingredient_set_2 = TODO
ingredient_set_3 = TODO
ingredient_intersection_set = TODO

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Check your work:**

# COMMAND ----------

assert ingredient_intersection_set == {"carrots"}, "Only carrots occurs in all the ingredients"
assert "broccoli" in ingredient_set_2, "Did you forget your broccoli?"

print("Test passed!")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC &copy; 2025 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the 
# MAGIC <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/><a href="https://databricks.com/privacy-policy">Privacy Policy</a> | 
# MAGIC <a href="https://databricks.com/terms-of-use">Terms of Use</a> | 
# MAGIC <a href="https://help.databricks.com/">Support</a>
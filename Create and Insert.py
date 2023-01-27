# Databricks notebook source
# DBTITLE 1,CREATE DataBase
# MAGIC %sql
# MAGIC create database delta_test;

# COMMAND ----------

# MAGIC %sql
# MAGIC use delta_test;

# COMMAND ----------

# DBTITLE 1,Create DDL of a table
# MAGIC %sql
# MAGIC -- DDL of Managed table
# MAGIC DROP TABLE IF EXISTS Student;
# MAGIC CREATE TABLE IF NOT EXISTS Student
# MAGIC (
# MAGIC   ID INTEGER,
# MAGIC   NAME STRING,
# MAGIC   Age INTEGER
# MAGIC )
# MAGIC USING DELTA;
# MAGIC 
# MAGIC -- DDL of External table
# MAGIC DROP TABLE IF EXISTS Student;
# MAGIC CREATE TABLE IF NOT EXISTS Student
# MAGIC (
# MAGIC   ID INTEGER,
# MAGIC   NAME STRING,
# MAGIC   Age INTEGER
# MAGIC )
# MAGIC USING DELTA
# MAGIC LOCATION '/FileStore/tables/output/Student'

# COMMAND ----------

# DBTITLE 1,Create DDL using Partition
# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS Student;
# MAGIC CREATE TABLE IF NOT EXISTS Student
# MAGIC (
# MAGIC   ID INTEGER,
# MAGIC   NAME STRING
# MAGIC )
# MAGIC USING DELTA
# MAGIC PARTITIONED BY (Age INTEGER)
# MAGIC LOCATION '/FileStore/tables/output/Student'

# COMMAND ----------

# DBTITLE 1,Desc table 
# MAGIC %sql
# MAGIC DESC Student

# COMMAND ----------

# DBTITLE 1,List file path
# MAGIC %py
# MAGIC dbutils.fs.ls('/FileStore/tables/output/Student')

# COMMAND ----------

# DBTITLE 1,Insert data Into table
# MAGIC %sql
# MAGIC INSERT INTO Student(ID,Name,Age)
# MAGIC VALUES(1,'John',34),(2,'Alex',29)

# COMMAND ----------

# DBTITLE 1,List the location of the table
dbutils.fs.ls('/FileStore/tables/output/Student')

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT OVERWRITE Student(ID,Name,Age)
# MAGIC VALUES(1,'John',34),(2,'Alex',29)

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS Admission;
# MAGIC CREATE TABLE IF NOT EXISTS Admission
# MAGIC (
# MAGIC   ID INTEGER,
# MAGIC   Name String,
# MAGIC   Age INTEGER
# MAGIC )
# MAGIC USING DELTA;
# MAGIC 
# MAGIC INSERT INTO Admission(ID,Name,Age)
# MAGIC VALUES(1,'John',34),(2,'David',29),(3,'Alex',29)

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT OVERWRITE Student PARTITION(Age=29)
# MAGIC SELECT ID,NAME 
# MAGIC FROM Admission 
# MAGIC WHERE Age=29

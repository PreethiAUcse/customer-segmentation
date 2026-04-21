from pyspark.sql.functions import col, count, when

# Read from Silver (created in Notebook 2)
df_silver = spark.sql("SELECT * FROM silver_customer_data")

# ... feature engineering code ...
df_gold = df_silver.select(
    col("customer_id"),
    col("Age"),
    col("Gender"),
    col("Total_Purchases"),
    col("Lifetime_Value"),
    col("Churned"),
    col("Login_Frequency")
)
# Create Gold table
df_gold.write.mode("overwrite").option("overwriteSchema", "true").saveAsTable("gold_customer_data")

spark.sql("SELECT COUNT(*) as total_records FROM gold_customer_data").show()

spark.sql("SELECT * FROM gold_customer_data").show(5)

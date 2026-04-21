from pyspark.sql.functions import count, when, col
print("=" * 80)
print("NULL VALUES IN THE COLUMN:")
print("=" * 80)
df_null=spark.sql("""select * from bronze_customer_data""")
null_counts = df_null.select([count(when(col(c).isNull(), c)).alias(c) for c in df_null.columns])
null_counts.show(1, vertical=True)

print("Duplicate rows:")
duplicate_count=  df_null.count() - df_null.dropDuplicates().count()
print(f"Number of duplicate rows: {duplicate_count}")

SELECT 
    ROUND(AVG(Total_Purchases), 2) as avg_purchases,
    ROUND(AVG(Product_Reviews_Written), 2) as avg_reviews,
    ROUND(AVG(Social_Media_Engagement_Score), 2) as avg_social_score,
    ROUND(AVG(Mobile_App_Usage), 2) as avg_mobile_usage
FROM silver_customer_data

print("Data schema:")
df_null.printSchema()

df_null.describe().show()

from pyspark.sql.functions import col, when, mean, isnan, isnull
from pyspark.sql.types import IntegerType, DoubleType

#remove duplicates
df_bronze = spark.sql("SELECT * FROM bronze_customer_data")
df_cleaned=df_bronze.filter(col("Total_Purchases")>=0)
print(f"Removed {df_bronze.count() - df_cleaned.count()} rows with negative Total_Purchases")

#handling missing data
age_mean=df_cleaned.filter(col("Age").isNotNull()).agg({'Age':'mean'}).collect()[0][0]
session_mean = df_cleaned.select(col("Session_Duration_Avg")).where(col("Session_Duration_Avg").isNotNull()).agg({"Session_Duration_Avg": "mean"}).collect()[0][0]
pages_mean = df_cleaned.select(col("Pages_Per_Session")).where(col("Pages_Per_Session").isNotNull()).agg({"Pages_Per_Session": "mean"}).collect()[0][0]
wishlist_mean = df_cleaned.select(col("Wishlist_Items")).where(col("Wishlist_Items").isNotNull()).agg({"Wishlist_Items": "mean"}).collect()[0][0]
days_mean = df_cleaned.select(col("Days_Since_Last_Purchase")).where(col("Days_Since_Last_Purchase").isNotNull()).agg({"Days_Since_Last_Purchase": "mean"}).collect()[0][0]

print(f"Age mean: {age_mean:.2f}")
print(f"Session mean: {session_mean:.2f}")
print(f"Pages mean: {pages_mean:.2f}")
print(f"Wishlist mean: {wishlist_mean:.2f}")
print(f"Days mean: {days_mean:.2f}")

df_filled=df_cleaned\
    .fillna(value=age_mean, subset=["Age"])\
    .fillna(value=session_mean, subset=["Session_Duration_Avg"])\
    .fillna(value=pages_mean, subset=["Pages_Per_Session"])\
    .fillna(value=wishlist_mean, subset=["Wishlist_Items"])\
    .fillna(value=days_mean, subset=["Days_Since_Last_Purchase"])\
    .fillna(value="Unknown", subset=["Gender","Country","City"])\
    .fillna(value=0, subset=["Customer_Service_Calls","Email_Open_Rate","Returns_Rate","Credit_Balance"])

display(df_filled)


#removing duplicates
filled_count=df_filled.count()
df_dropped=df_filled.dropDuplicates()
dropped_count=df_dropped.count()
print(f"Removed {filled_count - df_cleaned.count()} duplicate rows")

#validate cleaned data
print("Null values in each column:")
df_dropped.select([count(when(col(c).isNull(), c)).alias(c) for c in df_dropped.columns]).show(1, vertical=True)

#create silver table
df_dropped.write.mode("overwrite").option("overwriteSchema", "true").saveAsTable("silver_customer_data")
print("silver table created successfully")
print(f"total count: {df_dropped.count()}")
df_dropped.show(5)


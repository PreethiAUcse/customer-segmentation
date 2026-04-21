"""Data ingestion functions."""

def read_csv(spark, file_path):
    """
    Read CSV file and return DataFrame.
    
    Args:
        spark: Spark session
        file_path: Path to CSV file
        
    Returns:
        DataFrame with CSV data
    """
    return spark.read.csv(file_path, header=True, inferSchema=True)


def add_customer_id(df):
    """
    Add unique customer_id column.
    
    Args:
        df: Input DataFrame
        
    Returns:
        DataFrame with customer_id column
    """
    from pyspark.sql.functions import monotonically_increasing_id
    return df.withColumn("customer_id", monotonically_increasing_id() + 1)

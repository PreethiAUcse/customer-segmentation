"""Feature scaling functions."""

from pyspark.ml.feature import StandardScaler, VectorAssembler


def scale_features(df, feature_columns, output_col="features_scaled"):
    """
    Scale features using StandardScaler (mean=0, std=1).
    
    Args:
        df: Input DataFrame
        feature_columns: List of feature column names
        output_col: Name of output column
        
    Returns:
        DataFrame with scaled features
    """
    assembler = VectorAssembler(inputCols=feature_columns, outputCol="features_unscaled")
    df_assembled = assembler.transform(df)
    
    scaler = StandardScaler(inputCol="features_unscaled", outputCol=output_col, 
                           withMean=True, withStd=True)
    scaler_model = scaler.fit(df_assembled)
    
    return scaler_model.transform(df_assembled)

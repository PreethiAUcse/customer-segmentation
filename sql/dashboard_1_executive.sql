SELECT 
    customer_id,
    Age,
    Gender,
    Total_Purchases,
    Lifetime_Value,
    Churned
FROM gold_customer_data
ORDER BY Lifetime_Value DESC
LIMIT 10

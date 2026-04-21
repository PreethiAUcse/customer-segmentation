SELECT 
    ROUND(AVG(Total_Purchases), 2) as avg_purchases,
    ROUND(AVG(Product_Reviews_Written), 2) as avg_reviews,
    ROUND(AVG(Social_Media_Engagement_Score), 2) as avg_social_score,
    ROUND(AVG(Mobile_App_Usage), 2) as avg_mobile_usage
FROM silver_customer_data

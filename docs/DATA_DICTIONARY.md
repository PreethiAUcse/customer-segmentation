# Data Dictionary

## Customer Data Columns


| Column | Type | Description |
|--------|------|-------------|
| customer_id | Long | Unique customer identifier |
| Age | Double | Customer age in years |
| Gender | String | Customer gender (M/F/Other) |
| Country | String | Customer country of residence |
| City | String | Customer city of residence |
| Membership_Years | Double | Years as a member (0-10) |
| Login_Frequency | Double | Average monthly login frequency (0-46) |
| Session_Duration_Avg | Double | Average session duration in minutes (1-75.6) |
| Pages_Per_Session | Double | Average number of pages visited per session (1-24.1) |
| Cart_Abandonment_Rate | Double | Percentage of carts abandoned (0-143.7%) |
| Wishlist_Items | Double | Number of items in customer wishlist (0-28) |
| Total_Purchases | Double | Total purchase amount in dollars (-13-128.7) |
| Average_Order_Value | Double | Average order value in dollars (26-9666) |
| Days_Since_Last_Purchase | Double | Number of days since last purchase (0-287) |
| Discount_Usage_Rate | Double | Percentage of purchases using discounts (0.24-116.64%) |
| Returns_Rate | Double | Product return rate percentage (0-99.6%) |
| Email_Open_Rate | Double | Email open rate percentage (0-91.7%) |
| Customer_Service_Calls | Double | Number of customer service calls made (0-21) |
| Product_Reviews_Written | Double | Number of product reviews written (0-21) |
| Social_Media_Engagement_Score | Double | Social media engagement score (0-100) |
| Mobile_App_Usage | Double | Mobile app usage percentage (0-61.9%) |
| Payment_Method_Diversity | Double | Number of unique payment methods used (1-5) |
| Lifetime_Value | Double | Total customer lifetime value in dollars (0-8987) |
| Credit_Balance | Double | Account credit balance in dollars (0-7197) |
| Churned | Integer | Customer churn status (0=Retained, 1=Churned) |
| Signup_Quarter | String | Quarter when customer signed up (Q1/Q2/Q3/Q4) |



## Data Quality Notes

- **Total Records**: 50,000 customers
- **Missing Values**: Present in some columns (handled in Silver layer)
- **Duplicates**: Possible (removed in Silver layer)
- **Invalid Values**: 
  - Age range (5-200) contains outliers
  - Total_Purchases has negative values (returns/refunds)
  - Cart_Abandonment_Rate exceeds 100% in some cases
- **Data Type Notes**:
  - All metrics are stored as Double (floating-point)
  - customer_id is Long (large integer ID)
  - Categorical variables (Gender, Country, City, Signup_Quarter) are String


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Read Gold data
df = spark.sql("SELECT * FROM gold_customer_data").toPandas()

print("=" * 80)
print("CREATING SIMPLE SAMPLE DASHBOARDS")
print("=" * 80)

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (16, 10)

# Create 6 simple plots
fig, axes = plt.subplots(2, 3, figsize=(18, 10))

# 1. Lifetime Value Distribution
axes[0, 0].hist(df['Lifetime_Value'], bins=50, color='skyblue', edgecolor='black')
axes[0, 0].set_title('Lifetime Value Distribution', fontsize=12, fontweight='bold')
axes[0, 0].set_xlabel('Lifetime Value ($)')
axes[0, 0].set_ylabel('Number of Customers')

# 2. Gender Distribution
gender_counts = df['Gender'].value_counts()
axes[0, 1].pie(gender_counts.values, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
axes[0, 1].set_title('Customer Distribution by Gender', fontsize=12, fontweight='bold')

# 3. Age vs Lifetime Value
axes[0, 2].scatter(df['Age'], df['Lifetime_Value'], alpha=0.5, color='green')
axes[0, 2].set_title('Age vs Lifetime Value', fontsize=12, fontweight='bold')
axes[0, 2].set_xlabel('Age')
axes[0, 2].set_ylabel('Lifetime Value ($)')

# 4. Churn Analysis
churn_counts = df['Churned'].value_counts()
churn_labels = ['Retained', 'Churned']
axes[1, 0].bar(churn_labels, churn_counts.values, color=['green', 'red'])
axes[1, 0].set_title('Customer Retention vs Churn', fontsize=12, fontweight='bold')
axes[1, 0].set_ylabel('Number of Customers')

# 5. Average Purchases by Gender
avg_purchases = df.groupby('Gender')['Total_Purchases'].mean()
axes[1, 1].barh(avg_purchases.index, avg_purchases.values, color='orange')
axes[1, 1].set_title('Average Purchases by Gender', fontsize=12, fontweight='bold')
axes[1, 1].set_xlabel('Average Purchases ($)')

# 6. Login Frequency Distribution
axes[1, 2].hist(df['Login_Frequency'], bins=30, color='purple', edgecolor='black')
axes[1, 2].set_title('Login Frequency Distribution', fontsize=12, fontweight='bold')
axes[1, 2].set_xlabel('Login Frequency')
axes[1, 2].set_ylabel('Number of Customers')

plt.tight_layout()
plt.show()

print("✅ Dashboard visualizations created!")

# Print summary statistics
print("\n" + "=" * 80)
print("SUMMARY STATISTICS")
print("=" * 80)
print(f"\nTotal Customers: {len(df):,}")
print(f"Average Age: {df['Age'].mean():.2f} years")
print(f"Average Lifetime Value: ${df['Lifetime_Value'].mean():.2f}")
print(f"Average Total Purchases: ${df['Total_Purchases'].mean():.2f}")
print(f"Churn Rate: {(df['Churned'].sum() / len(df)) * 100:.2f}%")
print(f"Average Login Frequency: {df['Login_Frequency'].mean():.2f}")

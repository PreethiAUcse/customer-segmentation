df1.createOrReplaceTempView("bronze_customer_data")
print("table created successfully")
%sql
select * from bronze_customer_data

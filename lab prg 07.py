import pandas as pd
order_data = pd.DataFrame({
    'customer_id': [101, 102, 101, 103, 102],
    'order_date': pd.to_datetime(['2023-01-10', '2023-01-15', '2023-02-01', '2023-01-20', '2023-03-05']),
    'product_name': ['Widget', 'Gadget', 'Widget', 'Widget', 'Gadget'],
    'order_quantity': [3, 5, 2, 4, 1]
})
orders_per_customer = order_data['customer_id'].value_counts()
avg_quantity_per_product = order_data.groupby('product_name')['order_quantity'].mean()
earliest_order = order_data['order_date'].min()
latest_order = order_data['order_date'].max()
print("1.Orders per customer:")
print(orders_per_customer)
print("\n2.Average quantity per product:")
print(avg_quantity_per_product)

print(f"\n3.Earliest order date: {earliest_order}")
print(f"Latest order date: {latest_order}")

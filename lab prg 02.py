import numpy as np
sales_data = np.array([
    [10, 20, 200],
    [15, 25, 375],
    [20, 30, 600]
])
average_price = np.mean(sales_data[:, 1])
print("Average price of all products sold:", average_price)

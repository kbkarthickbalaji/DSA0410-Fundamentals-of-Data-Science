import numpy as np
house_data = np.array([
    [3, 1500, 250000],
    [5, 2500, 400000],
    [4, 2000, 350000],
    [6, 3000, 500000],
    [3, 1800, 275000],
    [7, 3500, 600000]
])
houses_with_more_than_4_bedrooms = house_data[house_data[:, 0] > 4]
average_sale_price = np.mean(houses_with_more_than_4_bedrooms[:, 2])
print("Average sale price of houses with more than 4 bedrooms:", average_sale_price)

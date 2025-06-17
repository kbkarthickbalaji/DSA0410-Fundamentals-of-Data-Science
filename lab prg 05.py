import numpy as np
fuel_efficiency = np.array([22, 25, 30, 35, 40])
average_efficiency = np.mean(fuel_efficiency)
percentage_improvement = ((fuel_efficiency[4] - fuel_efficiency[0]) / fuel_efficiency[0]) * 100
print(f"Average Fuel Efficiency: {average_efficiency:.2f} MPG")
print(f"Percentage Improvement between Model 1 and Model 5: {percentage_improvement:.2f}%")

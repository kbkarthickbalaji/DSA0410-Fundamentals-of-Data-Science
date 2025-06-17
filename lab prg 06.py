item_prices = [10.0, 5.0, 2.5]
quantities = [2, 4, 3]
discount_rate = 10 
tax_rate = 8        
subtotals = [p * q for p, q in zip(item_prices, quantities)]
total_before_discount = sum(subtotals)
discount_amount = total_before_discount * (discount_rate / 100)
total_after_discount = total_before_discount - discount_amount
tax_amount = total_after_discount * (tax_rate / 100)
final_total = total_after_discount + tax_amount
print(f"Final Total: ${final_total:.2f}")

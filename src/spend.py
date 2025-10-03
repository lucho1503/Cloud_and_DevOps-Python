#/usr/bin/env python3

def total_cost(d, list_items, tax):
  "given a dictionary and a list items, calculate el total cost of items and plus tax"
  total = 0 # Initialize total
  tax_cost = 0 # Initialize tax cost
  # for key, value in d.items(): # Call the items() method
  #   if key in list_items:
  #     total += value
  for item in list_items:
    if item in d:
      total += d[item]
  tax_cost = total * tax
  return round(total + tax_cost, 2)
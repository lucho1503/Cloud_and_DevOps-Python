#/usr/bin/env python3

from spend import total_cost

costs = {'socks': 5, 'shoes': 60, 'sweater': 70}
costs1 = {'socks': 6, 'shoes': 70, 'sweater': 40}
costs2 = {'socks': 7, 'shoes': 90, 'sweater': 50}
costs3 = {'socks': 8, 'shoes': 100, 'sweater': 60}




print(total_cost(costs, ['socks', 'shoes'], 0.09))  # Output: 70.85
print(total_cost(costs1, ['socks', 'shoes', 'sweater'], 0.07))  # Output: 121.2
print(total_cost(costs2, ['socks'], 0.05))  # Output: 7.35
print(total_cost(costs3, ['shoes', 'sweater'], 0.1))  # Output: 176.0
print(total_cost(costs, ['socks', 'shoes', 'sweater'], 0.08))  # Output: 140.4
print(total_cost(costs1, ['shoes'], 0.06))  # Output: 74.2
print(total_cost(costs2, ['sweater', 'socks'], 0.04))  # Output: 58.28
print(total_cost(costs3, [], 0.05))  # Output: 0.0
print(total_cost({}, ['socks', 'shoes'], 0.1))  # Output: 0.0
print(total_cost(costs, ['hat'], 0.07))  # Output: 0.0
print("# All tests passed.")
print("###########################################")


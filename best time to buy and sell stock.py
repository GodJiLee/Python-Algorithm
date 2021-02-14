prices = [7, 1, 5, 3, 6, 4]

# 1. Brute Force
max_price = 0

for i, price in enumerate(prices):
    for j in range(i, len(prices)):
        max_price = max(prices[j] - price, max_price)

# 2. Kadane's Algorithm
import sys
profit = 0
min_price = sys.maxsize # maximize value on the system

# update min/max
for price in prices:
    min_price = min(min_price, price)
    profit = max(profit, price - min_price)



# Mehmet Taha Ünal - 231AMB077
# Lab 3.4 – Functional Tools Practice
# Goal: Practice map, filter, zip, and comprehensions

prices = [12.5, 9.9, 15.0, 22.3, 5.0]
quantities = [2, 5, 1, 3, 4]

# --- 1. Compute totals using map() ---
totals = list(map(lambda p_q: p_q[0] * p_q[1], zip(prices, quantities)))

# --- 2. Filter totals above 30 ---
high_totals = list(filter(lambda total: total > 30, totals))

# --- 3. Pair prices and quantities with zip() ---
pairs = list(zip(prices, quantities))

# --- 4. Repeat using list comprehensions ---
totals_comp = [p * q for p, q in zip(prices, quantities)]
high_totals_comp = [t for t in totals_comp if t > 30]

# --- 5. Print results ---
print("------ Functional Tools Practice ------")
print("Prices:", prices)
print("Quantities:", quantities)
print("Totals:", totals)
print("Totals > 30:", high_totals)
print("Price-quantity pairs:", pairs)
print("Totals (comprehension):", totals_comp)
print("Totals > 30 (comprehension):", high_totals_comp)
print("----------------------------------------")

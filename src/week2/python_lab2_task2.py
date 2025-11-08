# Mehmet Taha Ünal - 231AMB077
# Lab 3.2 – Comprehensions and Transformations
# Goal: Practice list, set, and dictionary comprehensions

import random

# --- 1. Generate 10 random integers between -10 and 10 ---
numbers = [random.randint(-10, 10) for _ in range(10)]

# --- 2. Implement comprehensions ---
squares = [n ** 2 for n in numbers]
positives = [n for n in numbers if n > 0]
even_squares = {n ** 2 for n in numbers if n % 2 == 0}
cubes = {n: n ** 3 for n in numbers}

# --- 3. Print results ---
print("------ Number Transformations ------")
print("Original numbers:", numbers)
print("Squares:", squares)
print("Positives:", positives)
print("Even squares:", even_squares)
print("Cubes:", cubes)
print("------------------------------------")

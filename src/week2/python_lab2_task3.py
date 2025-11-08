# Mehmet Taha Ünal - 231AMB077
# Lab 3.3 – Operator Frequency Counter
# Goal: Count frequency of arithmetic operators in user input

# --- 1. Get input from the user ---
expression = input("Enter an arithmetic expression: ")

# --- 2. Define possible operators ---
operators = ['+', '-', '*', '/', '(', ')']

# --- 3. Initialize frequency dictionary ---
operator_counts = {op: 0 for op in operators}

# --- 4. Count occurrences ---
for char in expression:
    if char in operators:
        operator_counts[char] += 1

# --- 5. Print results ---
print("\n------ Operator Frequency ------")
for op, count in operator_counts.items():
    print(f"'{op}': {count} time(s)")
print("--------------------------------")


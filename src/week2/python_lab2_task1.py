# Mehmet Taha Ünal - 231AMB077
# Lab 3.1 – Simple Datasets and Aggregates
# Goal: Work with lists and dictionaries, calculate aggregates

# --- 1. Create datasets ---
temperatures = [5.2, 6.8, 4.9, 7.3, 8.0, 6.1, 5.5]  # °C for a week
city_population = {
    "Riga": 632_614,
    "Vilnius": 593_425,
    "Tallinn": 437_619,
    "Kaunas": 312_120,
    "Tartu": 91_783
}

# --- 2. Compute aggregates ---
average_temperature = sum(temperatures) / len(temperatures)

largest_city = max(city_population.keys(), key=lambda x: city_population[x])
largest_population = city_population[largest_city]

total_population = sum(city_population.values())

# --- 3. Print results ---
print("------ Weekly Report ------")
print(f"Average temperature: {average_temperature:.1f} °C")
print(f"Largest city: {largest_city} ({largest_population:,} people)")
print(f"Total population of all cities: {total_population:,}")
print("----------------------------")



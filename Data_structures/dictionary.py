# dictionary.py
# 1. Add key-value
d = {0: 10, 1: 20}
d[2] = 30

# 2. Concatenate dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
merged = {**dic1, **dic2, **dic3}

# 3. Check key existence
key = 3
print(key in merged)

# 4. Iterate and print
for k in merged:
    print("Key:", k)
for v in merged.values():
    print("Value:", v)
for k, v in merged.items():
    print(f"{k}: {v}")

# 5. Dictionary with squares
squares = {x: x**2 for x in range(1, 16)}

# 6. Sum values
print(sum(squares.values()))


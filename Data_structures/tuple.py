# tuple.py
# 1. Print 4th from start and end
t = (10, 20, 30, 40, 50, 60, 70)
print(t[3], t[-4])

# 2. Check if element exists
print(30 in t)

# 3. List to tuple
lst = [1, 2, 3]
tup = tuple(lst)

# 4. Find index
print(t.index(40))

# 5. Replace last value of each tuple
lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
modified = [x[:-1] + (100,) for x in lst]
print(modified)

# set.py
# 1. Remove item
s = {1, 2, 3}
s.discard(2)

# 2. Intersection
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)

# 3. Union
print(a | b)

# 4. Min and Max
print(min(s), max(s))

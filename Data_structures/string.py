# string.py
# 1. Count upper and lower
s = "HeLLoWorld"
upper = sum(1 for c in s if c.isupper())
lower = sum(1 for c in s if c.islower())
print(f"Upper: {upper}, Lower: {lower}")

# 2. Check palindrome
print(s == s[::-1])

# 3. Repeat first 2 chars n times
s = "Wipro"
n = len(s)
print(s[:2] * n)

# 4. Remove 'x' if at start or end
s = "xHix"
if s.startswith('x'):
    s = s[1:]
if s.endswith('x'):
    s = s[:-1]
print(s)

# 5. Repeat last n chars, n times
s = "Wipro"
n = 3
print(s[-n:] * n)

# lists.py
# 1. Create a list and display items by index
lst = [10, 20, 30, 40, 50]
for i in range(len(lst)):
    print(f"Index {i}: {lst[i]}")

# 2. Append item to end of list
lst.append(60)

# 3. Reverse list
lst.reverse()

# 4. Count occurrences
print(lst.count(20))

# 5. Append list1 to front of list2
list1 = [1, 2]
list2 = [3, 4]
list2 = list1 + list2

# 6. Insert before second element
lst.insert(1, 25)

# 7. Remove item at specific index
del lst[2]

# 8. Remove first occurrence of element
lst.remove(40)

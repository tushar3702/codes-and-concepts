# ----------------------------
# Importing the array module
# ----------------------------
from array import array

# ----------------------------
# Emaple 1: Python Array
# Syntax: array(typecode, initializer_list)
arr = array('i', [1, 2, 3, 4])

print("Array Example:")
print("Type:", type(arr))         # <class 'array.array'>
print("Content:", arr)            # array('i', [1, 2, 3, 4])

# Example 2: Python list
# ----------------------------
# Lists are more flexible and can hold mixed data types
l1 = list([1, 2, 3])  # same as l1 = [1, 2, 3]

print("\nList Example:")
print("Type:", type(l1))          # <class 'list'>
print("Content:", l1)             # [1, 2, 3]

# ----------------------------
# Key Differences (as comments):
# ----------------------------
# 1. Array:
#    - Must contain same data type (homogeneous).
#    - More memory efficient.
#    - Faster for numeric operations.
#    - Limited compared to list.
#
# 2. List:
#    - Can contain mixed data types (heterogeneous).
#    - More flexible.
#    - Uses more memory.
#    - Slower for numeric operations.
#





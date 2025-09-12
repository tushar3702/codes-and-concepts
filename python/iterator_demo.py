# ------------------------------
# This script demonstrates Python iterators
# and shows how 'for' loops work internally
# ------------------------------

# List to iterate
l1 = [1, 2, 3, 4]

# Using iter() and next() manually
it = iter(l1)
print("Manual iteration using next():")
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
print(next(it))  # 4
# Uncommenting the next line will raise StopIteration
# print(next(it))  

# Using iter() with while loop and try-except
print("\nIteration using while loop and try-except:")
it = iter(l1)
while True:
    try:
        print(next(it), end=' ')
    except StopIteration:
        break
print()  # for newline

# Using a for loop (Pythonic way)
print("\nIteration using for loop:")
for x in l1:
    print(x, end=' ')
print()

# ------------------------------
# Explanation: How 'for' loop works internally
# ------------------------------
# When you write:
#     for x in l1:
#         # do something
#
# Python internally does:
#     it = iter(l1)
#     while True:
#         try:
#             x = next(it)
#             # do something
#         except StopIteration:
#             break
#
# So, the 'for' loop is just a cleaner way to use iterators.
# Any object implementing __iter__() and __next__() can be used in a for loop.
#
# Diagram:
# l1 (list) ---> iter() ---> iterator object ---> next() ---> StopIteration

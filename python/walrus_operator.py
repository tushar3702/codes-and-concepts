"""
---------------------------
Examples demonstrating the use of the Walrus Operator (:=) in Python 3.8+
Description:
    The Walrus Operator allows assignment within expressions.
    It can make code shorter and more readable when used wisely.
"""

# Example 1: Traditional way (without walrus)
print("\n--- Example 1: Traditional while loop ---")
data = input("Enter Data: ")
while data != 'quit':
    print("Your data is:", data)
    data = input("Enter Data: ")

# Example 2: Using walrus operator in while loop
print("\n--- Example 2: Using walrus operator in while loop ---")
while (data := input("Enter Something: ")) != 'quit':
    print("Your data is:", data)

# Example 3: Traditional way (without walrus) in if condition
print("\n--- Example 3: Traditional if statement ---")
data = input("Enter data: ")
if len(data) > 5:
    print("Long input!")

# Example 4: Using walrus operator in if condition
print("\n--- Example 4: Using walrus operator in if statement ---")
if (data := input("Enter Something: ")) and len(data) > 5:
    print("Long Input!")

print("\n✅ Program finished...")



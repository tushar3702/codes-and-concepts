# Example of positional and keyword arguments
def fun(a, b):
    print("a =", a, ", b =", b)

# Function calls
fun(3, 4)              # positional
fun(b=4, a=10)         # keyword
fun(2, b=3)            # mix (positional + keyword)
# fun(a=2, 3)          # ❌ Error: positional must come after positional args


# Example of variable length arguments (*args)
def average(*t):
    return sum(t) / len(t)

print("Average is:", average(2, 3, 4, 5))

# Example of keyword variable length arguments (**kwargs)
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print("\nDetails:")
print_details(name="Tushar", role="Backend Developer", lang="Python")

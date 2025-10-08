import keyword as kw

# keyword => can't not be used as identifier
kywd = kw.kwlist #35
# soft keyword => can be used as identifier
sf_kywd = kw.softkwlist #4

print(len(sf_kywd))

for i in sf_kywd:
    print(i)

# print(type(10))
type point = tuple[float, float]
type list_of_point = list[point]

p1:point=[3.4, 4.5]
p2:point=[3.0, 6.5]
p3:point=[2.3, 9.5]
mylist:list_of_point = [p1, p2, p3]

# print(type(mylist))
print(mylist)

statements = input("Enter statement")
match statements:
    case 'tushar':
        print("Tushar")
    case 'user':
        print("User")
    case _:
        print("Default Case")

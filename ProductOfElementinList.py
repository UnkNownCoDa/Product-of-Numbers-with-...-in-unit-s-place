#Program to find product of all elements which have 3 in their unit's place

product = 1
L = []
size = int(input("Enter size of list: "))
for i in range(0, size):
    temp = int(input("Enter element: "))
    L.append(temp)

for i in L:
    if i%10 == 7:
        product *= i

if product == 1:
    print(f"There are not elements with 7 in their unit's place")
else:
    print(f"The product of elements with 7 in their unit's place: {product}")

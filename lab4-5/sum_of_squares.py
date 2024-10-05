num = int(input("Please enter a number :"))

count = 0
list = []

for i in range(1, num):
    count += i**2
    string = f"{i}^2"
    list.append(string)

print(" + ".join(list), end=" = ")
print(count)

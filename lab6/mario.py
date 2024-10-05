height = None

while not height:
    value = int(input("Please enter a height: "))
    if value > 0 and value < 9:
        height = value



row = height * " "
mid = "  "

for n in range(height):
    row_arr = list(row)
    row_arr[-(1 + n)] = "#"
    row = "".join(row_arr)
    print(row + mid + "".join(reversed(row_arr)))

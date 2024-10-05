def print_table(n: int) -> None:
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(f"{i * j:5}", end=" ")
        print()

number = int(input("What number n should we make a table of? "))
print_table(number)

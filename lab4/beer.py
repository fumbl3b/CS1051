def sing(n: int) -> None:
    for i in range(n, 0, -1):
        print(f"{i} bottles of beer on the wall, {i} bottles of beer")
        print(f"Take one down, passit around, {i-1} bottles of beer on the wall")

bottles = int(input("How many bottles? "))
sing(bottles)

def printChars(amount: int, reversed: bool):
    print_string = ""
    if (amount == 11 or amount == 12):
        print_string += "|" + "\""*amount + "|"
    elif (amount > 0):
        char = ":"
        begin_end_char = "\\/"
        if(reversed): begin_end_char = "/\\"
        print_string += begin_end_char[0] + char*amount + begin_end_char[1]
    else:
        print_string += "||"

    # Post process to correct spacing
    while(len(print_string) < 14):
        print_string = " " + print_string + " "

    print(print_string)

def drawHourglass() -> None:
    # Print top
    for i in range(12, -2, -2):
        printChars(i, False)
    # Print bottom
    for i in range(2, 13, 2):
        printChars(i, True)


drawHourglass()

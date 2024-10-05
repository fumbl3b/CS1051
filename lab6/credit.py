with open('example_cards.txt', 'r') as file:
    valid_cards = [line.strip() for line in file.readlines()]

# Luhn's algorithm'

def luhn(card_number: int) -> bool:
    value = list(str(card_number))

    # Start with second to last digit
    # for digit in value[::-2]

    for i in value[-2::-2]:
        print(i, end="")
    print("")
    return True


# for card in valid_cards:
    # print(card)
    # luhn(int(card))

test_list = [1,2,3,4,5,6,7,8,9,10]
str_list = list(map(str, test_list))
print(' '.join(str_list))
for n in test_list[-2::-2]:
    print(n, end=' ')
print("")

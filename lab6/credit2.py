with open('example_cards.txt', 'r') as file:
    valid_cards = [line.strip() for line in file.readlines()]

# Luhn's algorithm'

def luhn(card_number: str) -> bool:
    split_nums = list(card_number)

    # Start with second to last digit
    # for digit in value[::-2]

    nums_to_double = []

    # split the nubmers to double
    for i in range(len(split_nums) - 2, -1, -2):
        nums_to_double.append(split_nums.pop(i))


    # print("numbers to double"," ".join(nums_to_double))
    # print("numbers remaining", " ".join(split_nums))

    doubled = list(map(lambda n: int(n)*2, list(nums_to_double)))
    # print("doubled digits: ", doubled)
    individual_digits = []
    for n in doubled:
        string_num = str(n)
        for digit in string_num:
            individual_digits.append(int(digit))
    # print("individual digits: ", individual_digits)
    doubled_sum = sum(individual_digits)
    final_checksum = doubled_sum + sum(map(lambda n: int(n), split_nums))
    # print("final checksum: ", final_checksum)

    if final_checksum % 10 == 0:
        return True
    else:
        return False

luhn(valid_cards[0])

def get_card_type(card_num):
    response = "Card Type not detected"
    if len(card_num) == 15:
        if card_num[0] == '3':
            response = "American Express"
        elif card_num[0] == '4':
            response = "VISA"
    elif len(card_num) == 16:
        response = "MasterCard"
    return response

for card in valid_cards:
    if not card.isdigit():
        print(f"{card} invalid format")
        continue
    print("testing " , card)
    if luhn(card):
        print(f"{card}: Valid CC number", get_card_type(card), sep="\n")
        # print(get_card_type(card))
    else:
        print(f"{card}: Invalid CC number")



# Testing reverse logic
# test_list = [1,2,3,4,5,6,7,8,9,10]
# str_list = list(map(str, test_list))
# print(' '.join(str_list))
# for n in test_list[-2::-2]:
#     print(n, end=' ')
# print("")

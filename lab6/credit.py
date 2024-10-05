def luhn(card_number: str) -> bool:
    split_nums = list(card_number)

    nums_to_double = []

    for i in range(len(split_nums) - 2, -1, -2):
        nums_to_double.append(split_nums.pop(i))

    doubled = list(map(lambda n: int(n)*2, list(nums_to_double)))

    digits = []
    for n in doubled:
        for digit in str(n):
            digits.append(int(digit))

    doubled_sum = sum(digits)
    final_checksum = doubled_sum + sum(map(lambda n: int(n), split_nums))

    return (final_checksum % 10 == 0)

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


card_number = None

while not card_number:
    user_input = input("Number: ")
    if user_input.isdigit():
        card_number = user_input

if luhn(card_number):
    print(f"{card_number}: Valid CC number", get_card_type(card_number), sep="\n")
else:
    print(f"{card_number}: Invalid CC number")

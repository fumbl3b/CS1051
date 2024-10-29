import constants

def validate_characters(string: str) -> bool:
    valid_hawaiian = {
        'a', 'e', 'i', 'o', 'u', 'p',
        'k', 'h', 'l', 'm', 'n', 'w', ' ', '\''
    }
    return all(c.lower() in valid_hawaiian for c in string)

def yes_no(string: str) -> bool:
    valid_yes = ['y', 'yes']
    valid_no = ['n', 'no']
    if string.lower().strip() in valid_yes:
        return True
    elif string.lower().strip() in valid_no:
        return False
    else:
        return False

def application():
    valid_input = ""
    while len(valid_input) == 0:
        user_input = input(constants.INPUT_PROMPT)
        if validate_characters(user_input):
            valid_input = user_input.rstrip()

    words = valid_input.split()
    pronounce = ''
    pronunciation_rules = {
        'w': lambda prev_char: 'w' if prev_char in [None, 'a', 'u', 'o'] else 'v',
        'a': lambda next_char: 'eye-' if next_char in ['i', 'e'] else 'ow-' if next_char in ['o', 'u'] else 'ah-',
        'e': lambda next_char: 'ay-' if next_char == 'i' else 'eh-oo-' if next_char == 'u' else 'eh-',
        'i': lambda _: 'ee-',
        'o': lambda next_char: 'oyo-' if next_char == 'i' else 'ow-' if next_char == 'u' else 'oh-',
        'u': lambda next_char: 'ooey-' if next_char == 'i' else 'oo-'
    }

    for word in words:
        skip = False
        for idx, char in enumerate(word):
            if skip:
                skip = False
                continue

            prev_char = word[idx - 1] if idx > 0 else None
            next_char = word[idx + 1] if idx < len(word) - 1 else None

            if char in pronunciation_rules:
                pronounce += pronunciation_rules[char](next_char)
                if char in ['a', 'e', 'o', 'u'] and next_char in ['i', 'e', 'o', 'u']:
                    skip = True
            else:
                pronounce += char

        pronounce = pronounce.rstrip('-')
        pronounce += ' '

    pronounce = pronounce.strip()
    print(valid_input, constants.IS_PRONOUNCED, pronounce)

    while True:
        again_input = input(constants.AGAIN_PROMPT)
        if yes_no(again_input):
            return False
        elif again_input.lower().strip() in ['n', 'no']:
            return True
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    end = False
    while not end:
        end = application()

if __name__ == "__main__":
    main()

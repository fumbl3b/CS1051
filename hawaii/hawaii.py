import strings

def validate_characters(string: str) -> bool :
    valid_hawaiian = [
        'a', 'e', 'i', 'o', 'u', 'p',
        'k', 'h', 'l', 'm', 'n', 'w', ' ', '\''
    ]
    for c in string:
        if c.lower() not in valid_hawaiian:
            return False
    return True

def yes_no(string: str) -> bool:
    valid_yes = ['y', 'yes']
    valid_no = ['n', 'no']
    if string.lower().rstrip() in valid_yes:
        return True
    elif string.lower().rstrip() in valid_no:
        return False
    else:
        return False

def application():
    valid_input = ""
    while len(valid_input) == 0:
        user_input = input(strings.INPUT_PROMPT)
        if validate_characters(user_input):
            valid_input = user_input.rstrip()

    words = valid_input.split()
    pronounce = ''
    for word in words:
        prev_char = None
        skip = False
        for idx,char in enumerate(word):
            if skip:
                skip = False
                continue
            if char == 'w':
                if prev_char in [None, 'a', 'u', 'o']:
                    pronounce += 'w'
                elif prev_char in ['i', 'e']:
                    pronounce += 'v'
            elif char == 'a':
                if idx != len(word) - 1:
                    if word[idx+1] in ['i', 'e']:
                        pronounce += 'eye-'
                        skip = True
                        continue
                    if word[idx+1] in ['o', 'u']:
                        pronounce += 'ow-'
                        skip = True
                        continue
                pronounce += 'ah-'
            elif char  == 'e':
                if idx != len(word) - 1:
                    if word[idx+1] == 'i':
                        pronounce += 'ay-'
                        skip = True
                        continue
                    if word[idx+1] == 'u':
                        pronounce += 'eh-oo-'
                        skip = True
                        continue
                pronounce += 'eh-'
            elif char == 'i':
                pronounce += 'ee-'
                continue
            elif char == 'o':
                if idx != len(word) - 1:
                    if word[idx+1] == 'i':
                        pronounce += 'oyo-'
                        skip = True
                        continue
                    if word[idx+1] == 'u':
                        pronounce += 'ow-'
                        skip = True
                        continue
                pronounce += 'oh-'
            elif char == 'u':
                if idx != len(word) - 1:
                    if word[idx+1] == 'i':
                        pronounce += 'ooey-'
                        skip = True
                        continue
                pronounce += 'oo-'
            else:
                pronounce += char
            prev_char = char
            if idx == len(word) - 1 and pronounce[-1] == '-':
                pronounce = pronounce[:-1]
        pronounce += ' '

    if pronounce[-1] == '-': pronounce = pronounce[:-1]
    print(valid_input, strings.IS_PRONOUNCED, pronounce)

    if yes_no(input(strings.AGAIN_PROMPT)): return False
    else: return True

def main():
    end = False
    while not end:
        end = application()

if __name__ == "__main__":
    main()

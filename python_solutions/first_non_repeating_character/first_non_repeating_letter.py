def first_non_repeating_letter(s):
    result = ""
    for letter in s:
        if letter.isalpha():
            if letter == letter.lower():
                if s.count(letter) + s.count(letter.upper()) == 1:
                    return letter
            else:
                if s.count(letter) + s.count(letter.lower()) == 1:
                    return letter 
        else:
            if s.count(letter) == 1:
                return letter
    return result
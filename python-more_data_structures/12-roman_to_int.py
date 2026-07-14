#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    num = 0
    length = len(roman_string)

    for i in range(length):
        if i < length - 1 and roman_dict.get(roman_string[i], 0) < roman_dict.get(roman_string[i+1], 0):
            num -= roman_dict.get(roman_string[i], 0)
        else:
            num += roman_dict.get(roman_string[i], 0)

    return num

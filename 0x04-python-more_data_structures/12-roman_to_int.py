#!/usr/bin/python3
def roman_to_int(roman_string):
    c = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    value = 0
    if (roman_string is not None) and (isinstance(roman_string, str)):
        if len(roman_string) > 1:
            for i in range(1, len(roman_string)):
                if c[roman_string[i]] < c[roman_string[i - 1]]:
                    value += c[roman_string[i]]
                else:
                    value += c[roman_string[i]] - 2 * c[roman_string[i - 1]]
        else:
            value = c[roman_string[0]]
        return value
    else:
        return 0

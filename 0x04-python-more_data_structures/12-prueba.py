#!/usr/bin/python3
def roman_to_int(roman_string):
    conrom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    value = 0
    if roman_string is not None or roman_string is str:
        for i in roman_string:
            if len(roman_string) > 1:
                for i in roman_string:
                    if conrom.get[i] >= conrom[i + 1]:
                        value += conrom[i]
                    else:
                        value -= conrom[i]
        return value
    else:
        return 0

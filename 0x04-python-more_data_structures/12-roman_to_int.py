#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return (0)

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    last_rom = 0

    for ch in roman_string:
        if ch not in rom_n:
            return (0)

        if rom_n[ch] > last_rom:
            num -= last_rom
        else:
            num += last_rom

        last_rom = rom_n[ch]

    num += last_rom
    return (num)

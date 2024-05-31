def roman_to_int(rom: str) -> int:
    my_dict = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }
    cnt = 0
    for i in range(len(rom)):
        if i + 1 < len(rom) and rom[i:i+2] in my_dict:
            cnt += my_dict[rom[i:i+2]]
            i += 1  
        else:
            cnt += my_dict[rom[i]]
    return cnt

print(roman_to_int("V"))  

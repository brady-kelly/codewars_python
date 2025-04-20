class RomanNumerals:

    @staticmethod
    def to_roman(val : int) -> str:
        roman = ''
        wip = val
        for dec in RomanNumerals.romans:
            c = wip // dec
            roman += RomanNumerals.romans[dec] * c
            wip = wip % dec
        return roman

    @staticmethod
    def from_roman(roman_num : str) -> int:
        return 0

    romans = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }

if __name__ == '__main__':
    RomanNumerals.to_roman(1990)

class RomanNumerals:

    @staticmethod
    def to_roman(val : int) -> str:
        roman = ''
        wip = val
        for dec in RomanNumerals.nums:
            c = wip // dec
            roman += RomanNumerals.nums[dec] * c
            wip = wip % dec
        return roman

    @staticmethod
    def from_roman(roman_num : str) -> int:
        total = 0
        wip = roman_num
        while len(wip) > 0:
            if wip[:2] in ["CM", "CD", "XC", "XL", "IX", "IV"]:
                total += RomanNumerals.romans[wip[:2]]
                wip = wip[2:]
            else:
                total += RomanNumerals.romans[wip[0]]
                wip = wip[1:]
        return total

    nums = {
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

    romans = {
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

if __name__ == '__main__':
    RomanNumerals.from_roman("MDCLXVI")



class Number:

    def __init__(self, roman, arabic):
        self.roman_numerals = roman
        self.arabic_number = arabic

    def get_roman(self):
        return self.roman_numerals

    def get_arabic(self):
        return self.arabic_number

    def set_roman(self, roman):
        self.roman_numerals = roman

    def set_arabic(self, arabic):
        self.arabic_number = arabic

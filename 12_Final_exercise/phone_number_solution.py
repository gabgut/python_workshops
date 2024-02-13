class PhoneNumber():
    def __init__(self, number):
        self.X_list = [str(i) for i in range(0,10)]
        self.number = self.clean_number(number)
        self.area_code = self.number[0:3]
        self.pretty = self.pretty_format

    def clean_number(self, raw_input):
        clean_number = ""
        for ch in raw_input:
            if ch in self.X_list:
                clean_number += ch
        flag = self.check_number_length(clean_number)
        if flag:
            self.check_country_code(clean_number)
            clean_number = self.remove_country_code(clean_number)
        self.check_area_code(clean_number)
        self.check_exchange_code(clean_number)
        return clean_number

    def check_country_code(self, number):
        if number[0] != "1":
            raise ValueError("Invalid NANP country code")

    def remove_country_code(self, number):
        if number[0] == "1":
            clean_number = number[1:]
            return clean_number
        return number

    def check_number_length(self, raw_input):
        if len(raw_input) not in [10, 11]:
            raise ValueError("Invalid NANP length")
        elif len(raw_input) == 10:
            return False
        elif len(raw_input) == 11:
            return True

    def check_area_code(self, number):
        if number[0] in ["0", "1"]:
            raise ValueError("Invalid NANP area code")

    def check_exchange_code(self, number):
        if number[3] in ["0", "1"]:
            raise ValueError("Invalid NANP area code")

    def pretty_format(self):
        return f"({self.number[0:3]}) {self.number[3:6]}-{self.number[6:]}"

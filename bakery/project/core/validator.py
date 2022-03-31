class Validator:
    @staticmethod
    def raise_if_string_is_empty_or_whitespace(string: str, message: str):
        if string.strip() == '':
            raise ValueError(message)

    @staticmethod
    def raise_if_number_is_zero_or_negative(number: float, message):
        if number <= 0:
            raise ValueError(message)

    @staticmethod
    def raise_if_number_is_not_in_range(number: int, min_value: int, max_value: int, message: str):
        if number < min_value or number > max_value:
            raise ValueError(message)
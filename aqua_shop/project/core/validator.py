class Validator:
    @staticmethod
    def raise_if_str_is_empty(string: str, message: str):
        if string == '':
            raise ValueError(message)

    @staticmethod
    def raise_if_number_is_less_than_or_equal_to_zero(number: float, message: str):
        if number <= 0:
            raise ValueError(message)

from abc import ABC, abstractmethod

from project.core.validator import Validator


class Drink(ABC):
    @abstractmethod
    def __init__(self, name: str, portion: int, price: float, brand: str):
        self.name = name
        self.portion = portion
        self.price = price
        self.brand = brand

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_string_is_empty_or_whitespace(
            value,
            'Name cannot be empty string or white space!')
        self.__name = value

    @property
    def portion(self):
        return self.__portion

    @portion.setter
    def portion(self, value):
        Validator.raise_if_number_is_zero_or_negative(
            value,
            'Portion cannot be less than or equal to zero!')
        self.__portion = value

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        Validator.raise_if_string_is_empty_or_whitespace(
            value,
            'Brand cannot be empty string or white space!')
        self.__brand = value

    def __repr__(self):
        return f' - {self.name} {self.brand} - {self.portion:.2f}ml - {self.price:.2f}lv'

from project.aquarium.base_aquarium import BaseAquarium
from project.fish.saltwater_fish import SaltwaterFish


class SaltwaterAquarium(BaseAquarium):
    def __init__(self, name: str):
        super().__init__(name, 25)

    @property
    def fish_type(self):
        return SaltwaterFish.__name__

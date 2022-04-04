from project.aquarium.base_aquarium import BaseAquarium
from project.fish.freshwater_fish import FreshwaterFish


class FreshwaterAquarium(BaseAquarium):
    def __init__(self, name: str):
        super().__init__(name, 50)

    @property
    def fish_type(self):
        return FreshwaterFish.__name__

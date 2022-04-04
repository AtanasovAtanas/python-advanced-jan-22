from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium


class AquariumFactory:
    aquarium_types = {
        'FreshwaterAquarium': FreshwaterAquarium,
        'SaltwaterAquarium': SaltwaterAquarium
    }

    def create_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in self.aquarium_types:
            raise ValueError('Invalid aquarium type.')
        return self.aquarium_types[aquarium_type](aquarium_name)

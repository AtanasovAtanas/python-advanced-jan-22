from project.decoration.ornament import Ornament
from project.decoration.plant import Plant


class DecorationFactory:
    decoration_types = {
        'Plant': Plant,
        'Ornament': Ornament
    }

    def create_decoration(self, decoration_type: str):
        if decoration_type not in self.decoration_types:
            raise ValueError('Invalid decoration type.')
        return self.decoration_types[decoration_type]()

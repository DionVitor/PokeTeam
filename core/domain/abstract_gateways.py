from abc import ABC, abstractmethod
from typing import Dict


class ABCGetPokemonGateway(ABC):
    @abstractmethod
    def search_pokemon(self, filter: Dict) -> Dict:
        pass

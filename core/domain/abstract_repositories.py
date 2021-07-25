from abc import ABC, abstractmethod
from typing import Dict, Union, List


class ABCRegisterRepository(ABC):
    @abstractmethod
    def register(self, user: Dict) -> Dict:
        pass


class ABCTeamManipulatorRepository(ABC):
    @abstractmethod
    def get_team(self, username: str) -> Dict:
        pass

    @abstractmethod
    def create_team(self, username: str) -> Dict:
        pass

    @abstractmethod
    def delete_team(self, username: str) -> Dict:
        pass


class ABCPokemonManipulatorRepository(ABC):
    @abstractmethod
    def get_all_pokemons_in_team(self, username: str) -> Union[Dict, List]:
        pass

    @abstractmethod
    def add_pokemon_in_team(self, username: str, pokemon: Dict) -> Dict:
        pass

    @abstractmethod
    def remove_pokemon_in_team(self, username: str, pokemon: Dict) -> Dict:
        pass

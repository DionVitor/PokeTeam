from typing import Dict

from core.domain.abstract_repositories import ABCPokemonManipulatorRepository
from core.domain.abstract_gateways import ABCGetPokemonGateway


class PokemonManipulator:
    repository: ABCPokemonManipulatorRepository = None
    gateway: ABCGetPokemonGateway = None

    def _get_pokemon(self, filter: str) -> Dict:
        response = self.gateway().search_pokemon(filter)
        return response

    def _get_all_pokemons_in_team(self, username: str) -> Dict:
        pokemons_in_team = self.repository().get_all_pokemons_in_team(username)
        return pokemons_in_team

    def add_pokemon_in_team(self, username: str, filter: str) -> Dict:
        pokemon = self._get_pokemon(filter)
        pokemons_in_team = self._get_all_pokemons_in_team(username)

        if hasattr(pokemons_in_team, "keys") and "Erro" in pokemons_in_team.keys():
            error = pokemons_in_team
            return error

        if "Erro" in pokemon.keys():
            error = pokemon
            return error

        if len(pokemons_in_team) == 6:
            return {"Erro": "Seu time já tem 6 pokemons."}

        if pokemon["id"] in [poke["id"] for poke in pokemons_in_team]:
            return {"Erro": f"Seu time já tem o pokemon {pokemon['name']}."}

        response = self.repository().add_pokemon_in_team(username, pokemon)
        return response

    def remove_pokemon_in_team(self, username: str, filter: str):
        pass

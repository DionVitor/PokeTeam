from typing import Dict, Union, List

from core.domain.abstract_repositories import ABCPokemonManipulatorRepository
from core.models import Team
from users.models import User


class PokemonManipulatorRepository(ABCPokemonManipulatorRepository):
    def get_all_pokemons_in_team(self, username: str) -> Union[List, Dict]:
        user = User.objects.get(username=username)
        try:
            team = Team.objects.get(user=user)
        except Team.DoesNotExist:
            return {"Erro": f"Não foi encontrado um time pokemon do usuário {username}."}

        return team.pokemons

    def add_pokemon_in_team(self, username: str, pokemon: Dict) -> Dict:
        user = User.objects.get(username=username)
        try:
            team = Team.objects.get(user=user)
        except Team.DoesNotExist:
            return {"Erro": f"Não foi encontrado um time pokemon do usuário {username}."}

        team.pokemons.append(pokemon)
        team.save()
        return {"Sucesso": f"Foi adicionado o pokemon {pokemon['name']} ao seu time."}

    def remove_pokemon_in_team(self, username: str, pokemon: Dict) -> Dict:
        pass

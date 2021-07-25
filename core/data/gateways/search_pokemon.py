import requests

from core.app.api.serializers import pokemon_serializer
from core.domain.abstract_gateways import ABCGetPokemonGateway

POKE_API_URL = "https://pokeapi.co/api/v2"


class GetPokemonGateway(ABCGetPokemonGateway):
    def search_pokemon(self, filter: str):
        response = requests.get(f"{POKE_API_URL}/pokemon/{filter}")
        if response.status_code == 404:
            return {"Erro": f"Não foi encontrado pokemon com o filtro {filter}."}

        return pokemon_serializer(response.json())

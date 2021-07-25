from typing import Dict


def get_pokemon(filter: str) -> Dict:
    gateway = get_pokemon.gateway()

    response = gateway.search_pokemon(filter)
    return response

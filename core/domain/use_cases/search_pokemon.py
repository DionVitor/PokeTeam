def get_pokemon(filter: str):
    gateway = get_pokemon.gateway()

    response = gateway.search_pokemon(filter)
    return response

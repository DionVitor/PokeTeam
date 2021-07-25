from typing import Dict, List, Union


def pokemon_serializer(pokemon: Dict) -> Dict:
    stats = pokemon["stats"]
    filtered_stats = {stats[index]["stat"]["name"]: stats[index]["base_stat"] for index in range(len(stats))}

    return {
        "id": pokemon["id"],
        "name": pokemon["name"],
        "type": pokemon["types"][0]["type"]["name"],
        "weight": pokemon["weight"],
        **filtered_stats
    }


def list_pokemon_serializer(pokemon_list: List) -> Union[Dict, List]:
    if len(pokemon_list) != 0:
        return {
            "Sucesso": [pokemon_list[index]["name"] for index in range(len(pokemon_list))]
        }

    return pokemon_list

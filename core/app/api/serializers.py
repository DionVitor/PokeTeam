from typing import Dict


def pokemon_serializer(pokemon: Dict):
    stats = pokemon["stats"]
    filtered_stats = {stats[index]["stat"]["name"]: stats[index]["base_stat"] for index in range(len(stats))}

    return {
        "id": pokemon["id"],
        "name": pokemon["name"],
        "type": pokemon["types"][0]["type"]["name"],
        "weight": pokemon["weight"],
        **filtered_stats
    }

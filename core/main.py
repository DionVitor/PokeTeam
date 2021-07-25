from core.domain.use_cases.register import register_user
from core.data.repositories.register import RegisterRepository
from core.domain.use_cases.search_pokemon import get_pokemon
from core.data.gateways.search_pokemon import GetPokemonGateway


def configure():
    register_user.repository = RegisterRepository
    get_pokemon.gateway = GetPokemonGateway

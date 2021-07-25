from django.urls import path

from core.app.api.views.register_view import RegisterAPIView
from core.app.api.views.search_pokemon_view import SearchPokemonAPIView
from core.app.api.views.manipulate_team_view import ManipulateTeamAPIView
from core.app.api.views.pokemon_team_view import PokemonTeamAPIView

app_name = "api"

urlpatterns = [
    path("register", RegisterAPIView.as_view()),
    path("search_pokemon", SearchPokemonAPIView.as_view()),
    path("manipulate_team", ManipulateTeamAPIView.as_view()),
    path("pokemon_team", PokemonTeamAPIView.as_view()),
]

from django.urls import path, include

from core.app.api.views.register_view import RegisterAPIView
from core.app.api.views.search_pokemon_view import SearchPokemonAPIView
from core.app.api.views.manipulate_team_view import ManipulateTeamAPIView
from core.app.api.views.pokemon_team_view import PokemonTeamAPIView
from core.app.api.views.user_view import router as user_router


app_name = "api"

urlpatterns = [
    path("", include(user_router.urls)),
    path("register", RegisterAPIView.as_view()),
    path("search_pokemon", SearchPokemonAPIView.as_view()),
    path("manipulate_team", ManipulateTeamAPIView.as_view()),
    path("pokemon_team", PokemonTeamAPIView.as_view()),
]

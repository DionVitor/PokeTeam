from django.urls import path

from core.app.api.views.register_view import RegisterAPIView
from core.app.api.views.search_pokemon_view import SearchPokemonAPIView


app_name = "api"

urlpatterns = [
    path("register", RegisterAPIView.as_view()),
    path("search_pokemon", SearchPokemonAPIView.as_view()),
]

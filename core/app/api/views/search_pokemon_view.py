from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from core.domain.use_cases.search_pokemon import get_pokemon


pokemon_param = openapi.Parameter("pokemon", in_=openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True)
summary = "Pesquisa de pokemon, por id ou nome."


class SearchPokemonAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(manual_parameters=[pokemon_param], tags=["Pokemon"], operation_summary=summary)
    def get(self, request):
        query_params = request.query_params

        filter = query_params.get("pokemon", None)
        if not filter:
            return Response({"Erro": "Não foi encontrado um filtro."}, status=status.HTTP_400_BAD_REQUEST)

        response = get_pokemon(filter)

        if response.get("Erro", None):
            response_status = status.HTTP_404_NOT_FOUND
        else:
            response_status = status.HTTP_200_OK

        return Response(data=response, status=response_status)

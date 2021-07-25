from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from core.domain.use_cases.pokemon_team import PokemonManipulator

pokemon_param = openapi.Parameter("pokemon", in_=openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True)
summary_post = "Adição de um pokemon ao time, por meio de id ou nome."
summary_delete = "Remoção de um pokemon do time, por meio de id ou nome."


class PokemonTeamAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(manual_parameters=[pokemon_param], tags=["Pokemon Team"], operation_summary=summary_post)
    def post(self, request):
        required_query_param = {"pokemon"}
        query_params = request.query_params
        missing_query_params = required_query_param - query_params.keys()

        if missing_query_params:
            return Response({"Erro": f"Não encontrado: {missing_query_params}."}, status=status.HTTP_400_BAD_REQUEST)

        response = PokemonManipulator().add_pokemon_in_team(request.user.username, query_params["pokemon"])

        if response.get("Erro", None):
            response_status = status.HTTP_400_BAD_REQUEST
        else:
            response_status = status.HTTP_201_CREATED

        return Response(response, status=response_status)

    @swagger_auto_schema(manual_parameters=[pokemon_param], tags=["Pokemon Team"], operation_summary=summary_delete)
    def delete(self, request):
        required_query_param = {"pokemon"}
        query_params = request.query_params
        missing_query_params = required_query_param - query_params.keys()

        if missing_query_params:
            return Response({"Erro": f"Não encontrado: {missing_query_params}."}, status=status.HTTP_400_BAD_REQUEST)

        response = PokemonManipulator().remove_pokemon_in_team(request.user.username, query_params["pokemon"])

        if response.get("Erro", None):
            response_status = status.HTTP_400_BAD_REQUEST
        else:
            response_status = status.HTTP_200_OK

        return Response(response, status=response_status)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from core.domain.use_cases.manipulate_team import TeamManipulator
from core.app.api.serializers import list_pokemon_serializer

param = openapi.Parameter("detailed", in_=openapi.IN_QUERY, type=openapi.TYPE_STRING, default="false")
summary_get = "Visualização do time pokemon atual."


class ManipulateTeamAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(tags=["Team"], operation_summary="Criação de um novo time pokemon.")
    def post(self, request):
        response = TeamManipulator().create_team(request.user.username)

        if response.get("Erro", None):
            response_status = status.HTTP_400_BAD_REQUEST
        else:
            response_status = status.HTTP_201_CREATED

        return Response(response, status=response_status)

    @swagger_auto_schema(manual_parameters=[param], tags=["Team"], operation_summary=summary_get)
    def get(self, request):
        detailed = request.query_params.get("detailed", None)
        response = TeamManipulator().get_team(request.user.username)

        if response.get("Erro", None):
            response_status = status.HTTP_404_NOT_FOUND
        else:
            response_status = status.HTTP_200_OK
            if not detailed or detailed == "false":
                response = list_pokemon_serializer(response["Sucesso"])

        return Response(response, status=response_status)

    @swagger_auto_schema(tags=["Team"], operation_summary="Remoção do time pokemon.")
    def delete(self, request):
        response = TeamManipulator().delete_team(request.user.username)

        if response.get("Erro", None):
            response_status = status.HTTP_404_NOT_FOUND
        else:
            response_status = status.HTTP_200_OK

        return Response(response, status=response_status)

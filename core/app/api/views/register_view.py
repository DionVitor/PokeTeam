from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from core.domain.use_cases.register import register_user


username = openapi.Parameter("username", in_=openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True)
password = openapi.Parameter("password", in_=openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True)
password_confirm = openapi.Parameter("password_confirm", in_=openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True)
params = [username, password, password_confirm]


class RegisterAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(manual_parameters=params, tags=["Auth"], operation_summary="Criação de um novo usuário.")
    def post(self, request, *args, **kwargs):
        required_query_params = {"username", "password", "password_confirm"}
        query_params = request.query_params
        missing_query_params = required_query_params - query_params.keys()

        if missing_query_params:
            return Response({"Erro": f"Não encontrado: {missing_query_params}."}, status=status.HTTP_400_BAD_REQUEST)

        user = {
            "username": query_params["username"],
            "password": query_params["password"],
            "password_confirm": query_params["password_confirm"],
        }

        response = register_user(user)

        if response.get("Erro", None):
            response_status = status.HTTP_400_BAD_REQUEST
        else:
            response_status = status.HTTP_201_CREATED

        return Response(response, status=response_status)

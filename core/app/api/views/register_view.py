from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from core.domain.use_cases.register import register_user


class RegisterAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

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
            response_status = status.HTTP_200_OK

        return Response(response, status=response_status)

from django.db.utils import IntegrityError

from typing import Dict

from users.models import User
from core.domain.abstract_repositories import ABCRegisterRepository


class RegisterRepository(ABCRegisterRepository):
    def register(self, user: Dict) -> Dict:
        username = user["username"]

        try:
            User.objects.create_user(username=username, password=user["password"])
        except IntegrityError:
            return {"Erro": "Username em uso."}

        return {"Sucesso": f"Usuário {username} cadastrado com sucesso."}

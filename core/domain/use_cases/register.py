from typing import Dict


def register_user(user: Dict) -> Dict:
    repository = register_user.repository()

    if user["password"] != user["password_confirm"]:
        return {"Erro": "As senhas não são iguais!"}

    user.pop("password_confirm")
    response = repository.register(user)
    return response

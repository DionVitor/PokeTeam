from django.db.utils import IntegrityError

from core.domain.abstract_repositories import ABCTeamManipulatorRepository
from users.models import User
from core.models import Team


class TeamManipulatorManipulatorRepository(ABCTeamManipulatorRepository):
    def get_team(self, username: str):
        try:
            user_id = User.objects.get(username=username).id
            team = Team.objects.get(user=user_id)
        except Team.DoesNotExist:
            return {"Erro": f"Não foi encontrado um time pokemon do usuário {username}"}

        return {"Sucesso": f"{team.pokemons}"}

    def create_team(self, username: str):
        try:
            user = User.objects.get(username=username)
            Team.objects.create(user=user)
        except IntegrityError:
            return {"Erro": f"Já existe um time pokemon para o usuário {username}."}

        return {"Sucesso": f"Foi criado um time pokemon para {username}."}

    def delete_team(self, username: str):
        try:
            user = User.objects.get(username=username)
            team = Team.objects.get(user=user)
            team.delete()
        except Team.DoesNotExist:
            return {"Erro": f"Não foi encontrado um time pokemon do usuário {username}"}

        return {"Sucesso": f"Time pokemon de {username} foi removido."}

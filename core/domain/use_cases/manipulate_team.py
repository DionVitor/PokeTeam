from core.domain.abstract_repositories import ABCTeamManipulatorRepository


class TeamManipulator:
    repository: ABCTeamManipulatorRepository = None

    def get_team(self, username: str):
        response = self.repository().get_team(username)
        return response

    def create_team(self, username: str):
        response = self.repository().create_team(username)
        return response

    def delete_team(self, username: str):
        response = self.repository().delete_team(username)
        return response

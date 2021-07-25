from abc import ABC, abstractmethod
from typing import Dict


class ABCRegisterRepository(ABC):
    @abstractmethod
    def register(self, user: Dict):
        pass


class ABCTeamManipulatorRepository(ABC):
    @abstractmethod
    def get_team(self, username: str):
        pass

    @abstractmethod
    def create_team(self, username: str):
        pass

    @abstractmethod
    def delete_team(self, username: str):
        pass

from abc import ABC, abstractmethod
from typing import Dict


class ABCRegisterRepository(ABC):
    @abstractmethod
    def register(self, user: Dict):
        pass

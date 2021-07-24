from core.domain.use_cases.register import register_user
from core.data.repositories.register import RegisterRepository


def configure():
    register_user.repository = RegisterRepository

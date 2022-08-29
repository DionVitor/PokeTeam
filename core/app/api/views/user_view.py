from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, routers

from users.models import User
from core.app.api.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]


router = routers.DefaultRouter()
router.register(r"users", UserViewSet)

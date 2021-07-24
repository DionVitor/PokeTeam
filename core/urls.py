from django.urls import path
from core.app.api.views.register_view import RegisterAPIView

app_name = "api"

urlpatterns = [
    path("register", RegisterAPIView.as_view())
]

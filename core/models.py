from django.db import models

from users.models import User


class Team(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    pokemons = models.JSONField(blank=True, null=True, default=[])

    def __str__(self):
        return f"Team de {self.user.username}"

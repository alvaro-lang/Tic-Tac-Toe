from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.dispatch import receiver


class GameConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'game'

    @receiver(post_migrate)
    def createGuestPlayers(sender, **kwargs):
        from .models.Player import Player

        if Player.objects.filter(name="Invitado1").exists() or Player.objects.filter(name="Invitado2").exists():
            return
        Player.objects.create(name="Invitado1")
        Player.objects.create(name="Invitado2")

from django.contrib import admin
from .models import Leaderboard,User,GameSession

# Register your models here.
admin.site.register(Leaderboard)
admin.site.register(User)
admin.site.register(GameSession)
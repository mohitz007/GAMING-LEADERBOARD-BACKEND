from django.urls import path
from . import views

urlpatterns = [
    path("api/leaderboard/submit", views.submit_score, name="submit_score"),
    path("api/leaderboard/top", views.get_leaderboard_top, name="get_leaderboard_top"),
    path("api/leaderboard/rank/<int:user_id>", views.get_player_rank, name="get_player_rank"),
]

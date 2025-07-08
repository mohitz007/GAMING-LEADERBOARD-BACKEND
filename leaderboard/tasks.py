from celery import shared_task

from leaderboard.models import Leaderboard

@shared_task
def update_leaderboard_ranks():
    leaderboard_entries = Leaderboard.objects.order_by("-total_score")
    for i, entry in enumerate(leaderboard_entries, start=1):
        entry.rank = i
        entry.save()
import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.db import transaction
from django.db.models import Sum,F

from leaderboard.tasks import update_leaderboard_ranks
from .models import User, GameSession, Leaderboard
from django.views.decorators.cache import cache_page

@csrf_exempt
@require_http_methods(["POST"])
def submit_score(request):
    try:
        data = json.loads(request.body)
        user_id = data.get("user_id")
        score = data.get("score")

        if user_id is None or score is None:
            return HttpResponseBadRequest("Missing user_id or score")

        user = User.objects.get(id=user_id)

        with transaction.atomic():
            # Add game session
            GameSession.objects.create(user=user, score=score, game_mode="default")

            leaderboard_entry, created = Leaderboard.objects.get_or_create(user=user, defaults={"total_score": 0})
            Leaderboard.objects.filter(user=user).update(total_score=F('total_score') + score)


            # Update ranks
            # update_leaderboard_ranks.apply_async() using celery beat

        return JsonResponse({"message": "Score submitted successfully"})

    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)



@cache_page(5)
@require_http_methods(["GET"])
def get_leaderboard_top(request):
    top_players = Leaderboard.objects.order_by("rank")[:10]
    data = [
        {
            "user_id": entry.user.id,
            "username": entry.user.username,
            "total_score": entry.total_score,
            "rank": entry.rank
        }
        for entry in top_players
    ]
    return JsonResponse(data, safe=False)


@require_http_methods(["GET"])
def get_player_rank(request, user_id):
    try:
        entry = Leaderboard.objects.get(user__id=user_id)
        return JsonResponse({"user_id": user_id, "rank": entry.rank})
    except Leaderboard.DoesNotExist:
        return JsonResponse({"error": "User not found in leaderboard"}, status=404)



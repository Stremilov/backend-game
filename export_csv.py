import csv

from django.http import HttpResponse

from task_2 import PlayerLevel, LevelPrize


def export_player_data(request):
    player_levels = PlayerLevel.objects.select_related('player', 'level').all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="player_data.csv"'

    writer = csv.writer(response)
    writer.writerow(['Player ID', 'Level Title', 'Is Completed', 'Prize Title'])

    for player_level in player_levels:
        prize_title = LevelPrize.objects.filter(level=player_level.level).first()
        prize_title = prize_title.prize.title if prize_title else 'No Prize'
        writer.writerow([player_level.player.player_id, player_level.level.title, player_level.is_completed, prize_title])

    return response

from django.db import models

from task_1 import Boost


class Player(models.Model):
    player_id = models.CharField(max_length=100)


class Level(models.Model):
    title = models.CharField(max_length=100)
    order = models.IntegerField(default=0)


class Prize(models.Model):
    title = models.CharField()


class PlayerLevel(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    completed = models.DateField()
    is_completed = models.BooleanField(default=False)
    score = models.PositiveIntegerField(default=0)

    def assign_prize(self):
        if self.is_completed:
            level_prize = LevelPrize.objects.filter(level=self.level).first()
            if level_prize:
                Boost.objects.create(type=level_prize.prize.title, player=self.player)
                print(f"Player {self.player.player_id} has received a prize: {level_prize.prize.title}")


class LevelPrize(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    prize = models.ForeignKey(Prize, on_delete=models.CASCADE)
    received = models.DateField()




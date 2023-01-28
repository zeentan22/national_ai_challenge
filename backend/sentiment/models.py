from django.db import models

class History(models.Model):
    user_input = models.CharField(max_length=200, blank=True)
    time = models.DateTimeField(auto_now_add=True)

class Data(models.Model):
    history = models.ForeignKey(History, null=True, on_delete=models.CASCADE, related_name="history_data", blank=True)
    aspect = models.CharField(max_length=50) # the word that the emotion is relating to

    EMOTION_CHOICES = [
        (-1, -1), # negative
        (0, 0), # neutral
        (1, 1), # positive
    ]
    emotion = models.IntegerField(choices=EMOTION_CHOICES)
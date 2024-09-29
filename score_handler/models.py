from django.contrib.auth.models import User
from django.db import models

from utils.models import BaseModel


class Content(BaseModel):
    title = models.CharField(max_length=254, null=True)
    body = models.TextField()

    def __str__(self):
        return self.title


class Score(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.ForeignKey('score_handler.Content', on_delete=models.CASCADE, null=True)

    score = models.IntegerField(help_text='<b>Note: </b>score should be between 1 to 5')
    comment = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = [['user', 'content']]
        indexes = [
            models.Index(fields=['user', 'content'])
        ]

    def clean(self):
        if self.score > 5 or self.score < 0:
            raise ValueError('score is out of range')






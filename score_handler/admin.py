from django.contrib import admin

from score_handler.models import User, Content, Score
from utils.admin import BaseAdmin


@admin.register(Content)
class ContentAdmin(BaseAdmin):
    model = Content


@admin.register(Score)
class ScoreAdmin(BaseAdmin):
    model = Score




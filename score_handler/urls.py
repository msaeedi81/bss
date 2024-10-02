from django.urls import path
from .views import ContentWithUserScoreListView, ScoreContentView

urlpatterns = [
    path('content/list/', ContentWithUserScoreListView.as_view(), name='content_with_user_scores'),
    path('content/score/', ScoreContentView.as_view(), name='score-content'),
]

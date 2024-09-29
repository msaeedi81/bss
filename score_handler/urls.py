from django.urls import path
from .views import ContentListView, SubmitScoreView

urlpatterns = [
    path('content/', ContentListView.as_view(), name='content-list'),
    path('score/', SubmitScoreView.as_view(), name='submit-score'),
]

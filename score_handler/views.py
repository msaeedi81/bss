from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from score_handler.models import Content, Score
from score_handler.serializers import ContentSerializer, ScoreSerializer


class ContentListView(generics.ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [IsAuthenticated]


class SubmitScoreView(generics.CreateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

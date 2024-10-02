from datetime import timedelta, timezone, datetime

from django.db.models import OuterRef, Avg, Count, Subquery
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from score_handler.models import Content, Score
from score_handler.serializers import ListOfContentsSerializer


class ContentWithUserScoreListView(ListAPIView):
    serializer_class = ListOfContentsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        user_score_subquery = Score.objects.filter(
            user=user,
            content=OuterRef('pk')
        ).values('score')[:1]

        return Content.objects.annotate(
            average_score=Avg('score__score'),
            score_count=Count('score__id'),
            user_score=Subquery(user_score_subquery),
        )


class ScoreContentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        content_id = request.data.get('content_id')
        user = request.user
        score_value = request.data.get('score')

        if not (1 <= score_value <= 5):
            return Response({'error': 'Score must be between 1 and 5'}, status=status.HTTP_400_BAD_REQUEST)

        recent_scores = Score.objects.filter(content_id=content_id,
                                             timestamp__gte=datetime.now(tz=timezone.utc) - timedelta(hours=1)).count()

        if recent_scores > 50:
            return Response({'error': 'Too many ratings in a short period. Please try again later.'},
                            status=status.HTTP_429_TOO_MANY_REQUESTS)

        Score.objects.update_or_create(
            user=user,
            content_id=content_id,
            defaults={'score': score_value}
        )

        return Response({
            'message': 'Score created/updated successfully',
        }, status=status.HTTP_200_OK)

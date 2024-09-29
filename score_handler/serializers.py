from rest_framework import serializers
from .models import Content, Score


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'title', 'body']


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['content', 'score', 'comment']

    def validate_score(self, value):
        if not (1 <= value <= 5):
            raise serializers.ValidationError("Score must be between 1 and 5.")
        return value

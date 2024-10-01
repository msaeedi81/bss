from rest_framework import serializers
from .models import Content


class ListOfContentsSerializer(serializers.ModelSerializer):
    average_score = serializers.DecimalField(max_digits=32, decimal_places=8)
    score_count = serializers.IntegerField()
    user_score = serializers.IntegerField(allow_null=True)

    class Meta:
        model = Content
        fields = ['id', 'title', 'body', 'average_score', 'score_count', 'user_score']

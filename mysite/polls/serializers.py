from rest_framework import serializers, viewsets, filters
import django_filters

from .models import Question, Choice


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ["id", "question_text", "pub_date"]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by("-id")
    serializer_class = QuestionSerializer


class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = ["question_id", "choice_text"]


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all().order_by("-id")
    serializer_class = ChoiceSerializer
    filterset_fields = ["question_id", "choice_text"]

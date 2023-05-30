from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from . import views
from .models import Question


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ["id", "question_text", "pub_date"]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


router = routers.DefaultRouter()
router.register(r"questions", QuestionViewSet)

urlpatterns = [
    # path('', views.index, name='index'),
    path("", include(router.urls))
]

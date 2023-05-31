from django.urls import path, include
from rest_framework import routers

from .serializers import QuestionViewSet, ChoiceViewSet


router = routers.DefaultRouter()
router.register(r"questions", QuestionViewSet)
router.register(r"choices", ChoiceViewSet)

urlpatterns = [
    # path('', views.index, name='index'),
    path("", include(router.urls))
]

from django.db import models


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published", auto_now_add=True)

    class Meta:
        ordering = ["-id"]


class Choice(models.Model):
    question_id = models.IntegerField()
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

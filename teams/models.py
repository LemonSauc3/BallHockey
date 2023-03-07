from django.db import models


# Create your models here.
class Teams(models.Model):
    # Division choices
    division_choices = (("A", "A"), ("B", "B"), ("C", "C"), ("D", "D"))

    name = models.CharField(max_length=100, primary_key=True)
    team_size = models.IntegerField()
    team_captain = models.CharField(max_length=100)
    division = models.CharField(max_length=1, choices=division_choices)


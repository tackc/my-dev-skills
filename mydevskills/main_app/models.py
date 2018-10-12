from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

SKILLLEVEL = (
    ('1', 'Fundamental Awareness'),
    ('2', 'Novice'),
    ('3', 'Intermediate'),
    ('4', 'Advanced'),
    ('5', 'Expert')
)

# Create your models here.
# class User(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name

class Skill(models.Model):
    skill = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    skill_level = models.CharField(
        max_length=1,
        choices=SKILLLEVEL,
        default=SKILLLEVEL[0][0]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.skill
    def get_absolute_url(self):
        return reverse('skill list')

class Note(models.Model):
    content = models.CharField(max_length=500)
    skill_id = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
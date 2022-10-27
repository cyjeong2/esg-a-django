from django.db import models
from django.core.validators import MaxValueValidator

# Restaurant model
class Restaurant(models.Model):
    """맛집"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    average_score = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(5),
        ]
    )

    def __str__(self):
        return f'[{self.pk}]{self.name}'

    def get_absolute_url(self):
        return f'/Restaurant/{self.pk}/'

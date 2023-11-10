from django.db import models

# Create your models here.
class Grade(models.Model):
    position = models.CharField(max_length=100)
    basic_salary = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.position
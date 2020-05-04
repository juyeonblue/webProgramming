from django.db import models
from django.utils import timezone

class Lion(models.Model):

    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    create_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return str(self.name)

from django.db import models

# Create your models here.

#null = True 

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

# Django admin에서 "Blog object(1)" 대신 "Title"을 나타내고 싶을 때!!
    def __str__(self):
        return self.title

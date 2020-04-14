from django.db import models
from django.utils import timezone

class Lion(models.Model):
# models.Model을 상속받아서 다음과같이 해주면 ORM으로 DB만들어 줌

    name = models.CharField(max_length = 100)  # 이름
    age = models.IntegerField() # 나이
    create_data = models.DateTimeField(default = timezone.now) # 생성날짜

    def __str__(self):
        return str(self.name)
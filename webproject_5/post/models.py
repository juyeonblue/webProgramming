from django.db import models

from django.utils import timezone
from myapp.models import Lion

# Create your models here.

class Post(models.Model):
    name = models.ForeignKey (Lion, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)      # 제목
    content = models.TextField(max_length = 200)    # 내용
    create_data = models.DateTimeField(default = timezone.now)
    objects = models.Manager()  # 저번시간에 말해준 Manager인데 다시한번 집고 넘어가
    
    def __str__(self):    # 얘는 데이터 생성 시 생성값을 title 칼럼으로 해준다는 것
        return str(self.title)

from django.db import models

# Create your models here.


# 모델정의
class Article(models.Model):
    title = models.CharField(max_length=20) 
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # 새롭게 추가할때만 시간을 등록하고, 수정할때는 등록하지 않는다.
    updated_at = models.DateTimeField(auto_now=True)  # 언제든지 수정되었을 때의 시간을 저장하겠다.

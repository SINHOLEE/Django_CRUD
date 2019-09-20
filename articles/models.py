from django.db import models

# Create your models here.


# 모델정의
class Article(models.Model):
    title = models.CharField(max_length=20) 
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # 새롭게 추가할때만 시간을 등록하고, 수정할때는 등록하지 않는다.
    updated_at = models.DateTimeField(auto_now=True)  # 언제든지 수정되었을 때의 시간을 저장하겠다.


class Comment(models.Model):
    # 위 클래스에서 아이디인 값(참조하는 값), on_delete: 만약 1:N관계인 데이터에서 1의 데이터(참초해주는 데이터)가 지워 졌을 때 처리하는 방법
    article = models.ForeignKey(Article, on_delete=models.CASCADE)  # models.CASCADE 는 Article이 삭제되면 comment도 함께 삭제됨
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 마지막에 생성된 댓글부터 나타나게 하도록 , 
    class Meta:  # meta data => 데이터를 위한 데이터??
        ordering = ['-pk']

    def __str__(self):
        return self.content
    
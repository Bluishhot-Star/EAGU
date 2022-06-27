from django.conf import settings
from django.db import models
from django.utils import timezone

# 블로그 모델 클래스 정의
class Post(models.Model): # models : Post가 장고모델임을 의미 -> 이로 인해 Post가 db에 저장되어야 한다는 것을 알게됨
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self): # publish 메서드
        self.published_date = timezone.now()
        self.save()

    def __str__(self): # 포스트의 제목 리턴
        return self.title


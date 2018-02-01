from django.db import models

# Create your models here.
from django.utils import timezone


# models.Model 데이터베이스 형태로 해줌
# 하나의 요소가 calm으로 인식
# 변경된 테이블 사항은 따로 정리해놓고, 나중에 합쳐서 사용

class Post(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    create_date = models.DateTimeField(
        default=timezone.now
    )
    published_Date = models.DateTimeField(
        blank=True, null=True
    )


    def publish(self):
        self.published_date = timezone.now()
        # 데이터베이스에 기록을 하는 것 save()
        self.save()

    def __str__(self):
        return self.title

    # 장고에서 규정된 class name
    # 전체적으로 적용되도록 하는 것
    class Meta:
        verbose_name = '글'
        verbose_name_plural = f'{verbose_name} 목록'
        ordering = ['-create_date']

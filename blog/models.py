from django.conf import settings
from django.db import models
import re
from django.forms import ValidationError
from django.urls import reverse


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')


# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='제목',# 길이제한 100
        help_text='포스팅 제목을 입력하세요. 100자 내외.')
    content = models.TextField(verbose_name='내용') #길이제한 없음
    photo = models.ImageField(blank=True, upload_to='blog/post/%Y/%m/%d')
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, blank=True,
                validators=[lnglat_validator], help_text='경도/위도')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    tag_set = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True) #최초 생성시간 저장
    updated_at = models.DateTimeField(auto_now = True)  #갱신 때마다 시간 저장

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name





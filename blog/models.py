from django.db import models
import re
from django.forms import ValidationError


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$',value):
        raise ValidationError('Invalid LngLat Type')

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=100, verbose_name= '제목', # 길이제한 100
  help_text='포스팅 제목을 입력하세요. 100자 내외')
    content = models.TextField(verbose_name='내용') #길이제한 없음
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, blank=True,
                validators=[lnglat_validator], help_text='경도/위도')
    created_at = models.DateTimeField(auto_now_add=True) #최초 생성시간 저장
    updated_at = models.DateTimeField(auto_now = True)  #갱신 때마다 시간 저장




from django.db import models
from django.urls import reverse


class Faq(models.Model):
    title = models.CharField(max_length=120, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    registered_time = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return "제목" + self.title

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
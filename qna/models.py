from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Qna(models.Model):
    title = models.CharField(max_length=120, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    registered_time = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    def str(self):
        return "제목" + self.title

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])


class Comment(models.Model):
    blog = models.ForeignKey(Qna, on_delete=models.CASCADE, null=True, related_name='comments')  # 관계 설정
    comment_date = models.DateTimeField(auto_now_add=True)  # 댓글 날짜
    comment_body = models.CharField(max_length=200)  # 댓글 내용
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)   # 유저 관계설정

    class Meta:
        ordering = ['id']  # 정렬기준
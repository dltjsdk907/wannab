from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Qna, Comment


class QnaListView(ListView):
    model = Qna
    paginate_by = 5


class QnaCreateView(CreateView):
    model = Qna
    fields = ['title','contents', 'owner']
    success_url = reverse_lazy('qna:list')  # 글쓰기를 완료했을 때 이동할 페이지
    template_name_suffix = '_create'


# @staff_member_required
class QnaDetailView(DetailView):
    model = Qna


class QnaUpdateView(UpdateView):
    model = Qna
    fields = ['title','contents', 'owner']
    template_name_suffix = '_update'
    success_url = reverse_lazy('qna:list')


class QnaDeleteView(DeleteView):
    model = Qna
    success_url = reverse_lazy('qna:list')


@login_required
def newreply(request):
    if request.method == 'POST':
        comment = Comment()
        comment.comment_body = request.POST['comment_body']
        comment.blog =Qna.objects.get(pk=request.POST['qna'])  # id로 객체 가져오기
        comment.comment_user = request.user
        comment.save()
        return redirect('/qna/detail/' + str(comment.blog.id))
    else:
        return redirect('home')  # 홈으로
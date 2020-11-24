from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Noti


class NotiListView(ListView):
    model = Noti
    paginate_by = 5


class NotiDetailView(DetailView):
    model = Noti

from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Faq


class FaqListView(ListView):
    model = Faq
    paginate_by = 5


class FaqDetailView(DetailView):
    model = Faq
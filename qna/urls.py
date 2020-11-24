from django.urls import path

from . import views
from .views import QnaListView, QnaCreateView
from .views import *

app_name = 'qna'

urlpatterns = [
    path('', QnaListView.as_view(), name='list'),
    path('add/', QnaCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', QnaDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', QnaUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', QnaDeleteView.as_view(), name='delete'),
    path('newreply', views.newreply, name="newreply"),
]
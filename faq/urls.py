from django.urls import path
from .views import *

app_name = 'faq'

urlpatterns = [
    path('', FaqListView.as_view(), name='list'),
    path('detail/<int:pk>/', FaqDetailView.as_view(), name='detail'),
]
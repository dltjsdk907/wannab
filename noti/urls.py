from django.urls import path
from .views import *

app_name = 'noti'

urlpatterns = [
    path('', NotiListView.as_view(), name='list'),
    path('detail/<int:pk>/', NotiDetailView.as_view(), name='detail'),
]
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from config.views import HomeView, PrivateView, UseView

urlpatterns = [
    path('shop/', include('shop.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('cart/', include('cart.urls')),
    path('coupon/', include('coupon.urls')),
    path('order/', include('order.urls')),
    path('qna/', include('qna.urls')),
    path('faq/', include('faq.urls')),
    path('noti/', include('noti.urls')),
    path('', HomeView.as_view(), name='home'),
    path('private/', PrivateView.as_view(), name='private'),
    path('use/', UseView.as_view(), name='Use'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
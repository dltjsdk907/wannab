from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'

    def __int__(self):
       pass


class PrivateView(TemplateView):
    template_name = 'private.html'

    def __int__(self):
        pass


class UseView(TemplateView):
    template_name = 'use.html'

    def __int__(self):
       pass
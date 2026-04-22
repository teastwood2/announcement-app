from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
# Create your views here.
def home_page_view(request):
    return render(request, 'web/home.html')

class HomePageView(View):
    def get(self, request):
        return render(request, 'web/home.html')
class HomePageView(TemplateView):
    template_name = 'web/home.html'
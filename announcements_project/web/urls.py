from django.urls import path
from .views import home_page_view, HomePageView
urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),]
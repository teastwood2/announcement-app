from django.urls import path
from .views import announcement_list, create_announcement, AnnouncementListView, CreateAnnouncementView

urlpatterns = [path('', AnnouncementListView.as_view(), name = 'announcement_list'), path('add/', CreateAnnouncementView.as_view(), name = 'create_announcement')]
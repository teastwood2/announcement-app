from django.db import models
from django.conf import settings
# Create your models here.
class Announcement(models.Model):
    title = models.CharField(max_length= 100)
    body = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = 'announcements')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title
from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import datetime
import csv
# Create your models here.
class Assignment(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    due_date = models.DateTimeField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name="assignments")

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):

        return self.title
    @classmethod
    def create_assignment_from_csv(cls, csv_file, owner):
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)
        assignments = []
        for row in reader:
            naive_dt = datetime.strptime(f"{row['date']} {row['time']}", "%Y-%m-%d %H:%M")
            dt = timezone.make_aware(naive_dt)
            new_assignment, created = Assignment.objects.get_or_create(title = row['title'], description = row ['description'], due_date = dt, owner = owner)
            assignments.append(new_assignment)
        return assignments

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete= models.CASCADE, related_name="submissions")
    student_name = models.CharField(max_length=100)
    file = models.FileField(upload_to="submissions")

    submitted_at = models.DateTimeField(auto_now_add = True)
    instructor_notified = models.BooleanField(default = False)

    def __str__(self):

        return f"{self.student_name} submitted {self.assignment}"
    
class Course(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):

        return self.title

   
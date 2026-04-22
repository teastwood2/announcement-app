from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import BulkAssignmentUploadForm
from .models import Assignment
# Create your views here.
@login_required
def bulk_assignment_upload(request):
    success = False
    assignments = []
    if request.method == "GET":
        form = BulkAssignmentUploadForm()
    elif request.method == "POST":
        form = BulkAssignmentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            assignments = Assignment.create_assignment_from_csv(csv_file, owner = request.user)
            success = True

    form_data = {'form' : form, 'success' : success, 'assignments' : assignments}
    return render(request, 'courses/bulk_assignment_upload.html', form_data)

@login_required
def assignment_list(request):
    assignments = Assignment.objects.all().order_by('created_at')
    return render(request, "courses/assignment_list.html", {'assignments' : assignments})

@login_required
def assignment_submission(request, assignment_id):
    return render(request, "courses/assignment_submission.html", {'assignment_id' : assignment_id})
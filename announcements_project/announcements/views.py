from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from core.mixins import IsTeacherRoleMixin
from .models import Announcement
from .forms import Announcement as AForm
from django.views import View
from django.views.generic import ListView, FormView
# Create your views here.
@login_required
def announcement_list(request):
    announcements = Announcement.objects.all()
    return render(request, 'announcements/announcement_list.html', {'announcements' : announcements})
#@method_decorator(login_required, name = 'dispatch')
class AnnouncementListView(LoginRequiredMixin, ListView):
    template_name = 'announcements/announcement_list.html'

    model = Announcement

    context_object_name = 'announcements'

    # def get(self, request):
    #     announcements = Announcement.objects.all()
    #     return render(request, self.template_name, {'announcements' : announcements})
def is_teacher(user):
    return user.role == 'teacher'
@login_required
#@user_passes_test(is_teacher, login_url = 'login') # Using the manual rule involving checking the user's role
@permission_required('announcements.add_announcement', raise_exception = True)
def create_announcement(request):
    if request.method == "GET":
        form = AForm()
        return render(request, 'announcements/create_announcement.html', { 'form' : form })
    elif request.method == "POST":
        form = AForm(request.POST)

        if form.is_valid():
            announcement = form.save(commit = False)
            announcement.created_by = request.user
            announcement.save()
            form_data = {'form': AForm(), 'new_announcement': announcement, 'success' : True}
            return render(request, 'announcements/create_announcement.html', form_data)
        else:
            return render(request, 'announcements/create_announcement.html', { 'form' : form })
# @method_decorator(login_required, name = 'dispatch')
# @method_decorator(user_passes_test(is_teacher, login_url = 'login'), name = 'dispatch')   
class CreateAnnouncementView(LoginRequiredMixin, PermissionRequiredMixin , FormView):
    template_name = 'announcements/create_announcement.html'
    form_class = AForm
    success_url = '/announcements/'
    permission_required = 'announcements.add_announcement'


    # def get(self,request, *args, **kwargs):
    #     form = self.form_class()
    #     return render(request, self.template_name, {'form' : form})
    
    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)

        # if form.is_valid():
    def form_valid(self, form):
        announcement = form.save(commit = False)
        announcement.created_by = self.request.user
        announcement.save()
        return super().form_valid(form)
        #return redirect('announcement_list')
    #return render(request, self.template_name, {'form' : form})
from django import forms

class BulkAssignmentUploadForm(forms.Form):
    csv_file = forms.FileField(label = "Select a CSV File")

    def clean_csv_file(self):
        file = self.cleaned_data.get('csv_file')

        if not file.name.endswith('.csv'):
            raise forms.ValidationError('Please upload a valid CSV file')
        if file.content_type != 'text/csv':
            raise forms.ValidationError('File Content is not CSV')
        return file
# class AssignmentForm(forms.ModelForm):
#     class Meta:
#         model = Assignment()
#         fields = ['title','description','due_date']

# class SubmissionForm(forms.form):
#     class Meta:
#         model = Submission()
#         fields = []
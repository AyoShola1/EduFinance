# forms.py

from django import forms
from .models import Student, StudentBulkUpload

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'current_status', 'surname', 'firstname', 'other_name', 'gender',
            'date_of_birth', 'current_class', 'date_of_admission',
            'parent_mobile_number', 'address', 'others', 'passport'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'date_of_admission': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'rows': 3}),
            'others': forms.Textarea(attrs={'rows': 3}),
        }

class StudentBulkUploadForm(forms.ModelForm):
    class Meta:
        model = StudentBulkUpload
        fields = ['csv_file']

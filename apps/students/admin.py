from django.contrib import admin
from .models import Student, StudentBulkUpload

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('registration_number', 'surname', 'firstname', 'other_name', 'gender', 'current_class', 'date_of_admission', 'current_status')
    search_fields = ('registration_number', 'surname', 'firstname', 'other_name')
    list_filter = ('gender', 'current_class', 'current_status')
    ordering = ('surname', 'firstname', 'other_name')

@admin.register(StudentBulkUpload)
class StudentBulkUploadAdmin(admin.ModelAdmin):
    list_display = ('date_uploaded', 'csv_file')
    readonly_fields = ('date_uploaded',)

# students mode
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.urls import reverse
from apps.corecode.models import StudentClass




class Student(models.Model):
    STATUS_CHOICES = [("active", "Active"), ("inactive", "Inactive")]
    GENDER_CHOICES = [("male", "Male"), ("female", "Female")]

    current_status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="active"
    )
    registration_number = models.CharField(max_length=200, unique=True)
    surname = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    other_name = models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="male")
    date_of_birth = models.DateField(default=timezone.now)
    current_class = models.ForeignKey(
        StudentClass, on_delete=models.SET_NULL, blank=True, null=True
    )
    date_of_admission = models.DateField(default=timezone.now)

    mobile_num_regex = RegexValidator(
        regex="^[0-9]{8,12}$", message="Entered mobile number isn't in a right format!"
    )
    parent_mobile_number = models.CharField(
        validators=[mobile_num_regex], max_length=12, blank=True
    )
    parent_email = models.EmailField(blank=True, null=True)

    address = models.TextField(blank=True)
    others = models.TextField(blank=True)
    passport = models.ImageField(blank=True, upload_to="students/passports/")

    class Meta:
        ordering = ["surname", "firstname", "other_name"]

    def save(self, *args, **kwargs):
        # Generate registration number only if it's a new student
        if not self.pk:
            current_year = timezone.now().year
            last_student = Student.objects.order_by('-id').first()
            if last_student:
                last_registration_number = last_student.registration_number
                last_sequence_number = int(last_registration_number.split('/')[-1])
                self.registration_number = f"CMC/{current_year}/{last_sequence_number + 1}"
            else:
                self.registration_number = f"CMC/{current_year}/1"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.surname} {self.firstname} {self.other_name} ({self.registration_number})"

    def get_absolute_url(self):
        return reverse("student-detail", kwargs={"pk": self.pk})


class StudentBulkUpload(models.Model):
    date_uploaded = models.DateTimeField(auto_now=True)
    csv_file = models.FileField(upload_to="students/bulkupload/")


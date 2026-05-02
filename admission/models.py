from django.db import models


PROGRAMME_CHOICES = [
    ('GNM', 'General Nursing & Midwifery (GNM)'),
    ('ANM', 'Auxiliary Nurse Midwifery (ANM)'),
]

class AdmissionEnquiry(models.Model):
    full_name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    programme = models.CharField(max_length=10, choices=PROGRAMME_CHOICES)
    board_name = models.CharField(max_length=200)
    passing_year = models.CharField(max_length=4)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    address = models.TextField()
    message = models.TextField(blank=True)
    applied_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending', choices=[
        ('Pending', 'Pending'),
        ('Reviewed', 'Reviewed'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ])

    class Meta:
        ordering = ['-applied_on']
        verbose_name = 'Admission Enquiry'
        verbose_name_plural = 'Admission Enquiries'

    def __str__(self):
        return f"{self.full_name} - {self.programme}"


class HostelAdmission(models.Model):
    full_name = models.CharField(max_length=200)
    programme = models.CharField(max_length=10, choices=PROGRAMME_CHOICES)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    guardian_name = models.CharField(max_length=200)
    guardian_phone = models.CharField(max_length=15)
    address = models.TextField()
    applied_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-applied_on']

    def __str__(self):
        return f"Hostel - {self.full_name}"

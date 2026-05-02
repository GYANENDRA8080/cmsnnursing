from django.contrib import admin
from .models import AdmissionEnquiry, HostelAdmission


@admin.register(AdmissionEnquiry)
class AdmissionEnquiryAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'programme', 'phone', 'email', 'status', 'applied_on']
    list_filter = ['programme', 'status']
    search_fields = ['full_name', 'phone', 'email']
    list_editable = ['status']


@admin.register(HostelAdmission)
class HostelAdmissionAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'programme', 'phone', 'guardian_name', 'applied_on']
    search_fields = ['full_name', 'phone']

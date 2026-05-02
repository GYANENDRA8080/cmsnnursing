#!/usr/bin/env python
"""
CMSN College - Initial Setup Script
Run this after installing requirements:
    pip install -r requirements.txt
    python setup.py
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cmsn_college.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def main():
    print("=" * 55)
    print("  CMSN College - Django Setup")
    print("=" * 55)

    # Run migrations
    print("\n[1/3] Running database migrations...")
    from django.core.management import call_command
    django.setup()
    call_command('makemigrations')
    call_command('migrate')

    # Create sample notices
    print("\n[2/3] Populating sample data...")
    from core.models import Notice, Programme
    from django.contrib.auth.models import User

    Notice.objects.get_or_create(
        title="DIPLOMA IN GENERAL NURSING & MIDWIFERY ADMISSION 2026-27",
        defaults={"link": "https://upsmfac.org/site/writereaddata/UploadNews/corrigendum/pdf/C_202604181821041406.pdf"}
    )
    Notice.objects.get_or_create(
        title="Reminder – Filling of Annual Self Assessment (UPSMF)",
        defaults={"link": "https://upsmfac.org/site/writereaddata/UploadNews/corrigendum/pdf/C_202604081600245604.pdf"}
    )
    Notice.objects.get_or_create(
        title="INC Special Attention Notice for Nursing Institutions",
        defaults={"link": "https://www.indiannursingcouncil.org/special-attention"}
    )
    Notice.objects.get_or_create(
        title="Nursing/Paramedical Tuition Fee Revision Notification",
        defaults={"link": "https://upsmfac.org/site/writereaddata/UploadNews/corrigendum/pdf/C_202604021721504800.pdf"}
    )
    Notice.objects.get_or_create(
        title="Examination Results – March 2026 – Visit UPSMFAC Portal",
        defaults={"link": "https://online.upsmfac.org/Online/Result.aspx"}
    )

    Programme.objects.get_or_create(
        name="GNM",
        defaults={
            "full_name": "General Nursing & Midwifery",
            "duration": "3 Years",
            "intake": 50,
            "eligibility": "10+2 Science (PCB) with 45% marks, Age 17-30 years",
            "description": "Prepares nurses for hospital and community roles with clinical skill and leadership mindset.",
        }
    )
    Programme.objects.get_or_create(
        name="ANM",
        defaults={
            "full_name": "Auxiliary Nurse Midwifery",
            "duration": "2 Years",
            "intake": 40,
            "eligibility": "10+2 Science (PCB) with 45% marks, Age 17-30 years",
            "description": "Prepares students for community health centres and maternal-child care.",
        }
    )

    print("   ✓ Sample notices added")
    print("   ✓ Programmes added")

    # Create superuser
    print("\n[3/3] Creating admin superuser...")
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@cmsn.edu', 'admin@123')
        print("   ✓ Superuser created: admin / admin@123")
    else:
        print("   ✓ Admin user already exists")

    print("\n" + "=" * 55)
    print("  ✅ Setup Complete!")
    print("=" * 55)
    print("\n  Start the server:")
    print("    python manage.py runserver")
    print("\n  URLs:")
    print("    Home:       http://127.0.0.1:8000/")
    print("    Admission:  http://127.0.0.1:8000/admission/")
    print("    Contact:    http://127.0.0.1:8000/contact/")
    print("    Gallery:    http://127.0.0.1:8000/gallery/")
    print("    Admin:      http://127.0.0.1:8000/admin/")
    print("    Admin creds: admin / admin@123")
    print("\n  To upload gallery photos:")
    print("    Go to Admin > Core > Gallery Images > Add")
    print("=" * 55 + "\n")


if __name__ == '__main__':
    main()

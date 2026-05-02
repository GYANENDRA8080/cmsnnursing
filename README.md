# 🏥 CMSN College - Django Web Project

**Chandramauli Swaminath Nursing & Paramedical College, Gorakhpur**
- INC Approved | Affiliated to UPSMF Lucknow

---

## 📁 Project Structure

```
cmsn_college/
├── manage.py
├── setup.py              ← Run this first!
├── requirements.txt
├── cmsn_college/         ← Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                 ← Home, Gallery, Notices
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── templates/core/
│   │   ├── home.html
│   │   └── gallery.html
│   └── static/core/
│       └── images/college_logo.jpeg
├── admission/            ← Admission & Hostel forms
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/admission/admission.html
├── contact/              ← Contact form
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/contact/contact.html
└── templates/
    └── base.html         ← Shared navbar + footer
```

---

## 🚀 Setup Instructions

### Step 1 – Install Python & pip
Make sure Python 3.9+ is installed.

### Step 2 – Create virtual environment (recommended)
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### Step 3 – Install requirements
```bash
pip install -r requirements.txt
```

### Step 4 – Run automated setup
```bash
python setup.py
```
This will:
- Run all migrations
- Add sample notices & programmes
- Create admin user (admin / admin@123)

### Step 5 – Start the server
```bash
python manage.py runserver
```

---

## 🌐 Website URLs

| Page | URL |
|------|-----|
| Home | http://127.0.0.1:8000/ |
| Admission | http://127.0.0.1:8000/admission/ |
| Contact | http://127.0.0.1:8000/contact/ |
| Gallery | http://127.0.0.1:8000/gallery/ |
| Admin Panel | http://127.0.0.1:8000/admin/ |

**Admin Login:** `admin` / `admin@123`

---

## 📸 How to Upload Gallery Photos

1. Go to → http://127.0.0.1:8000/admin/
2. Login with admin / admin@123
3. Click **Core → Gallery Images → Add Gallery Image**
4. Upload image, add title & description
5. Save → Photo appears on Gallery page instantly!

---

## 📋 Admin Features

| Feature | Path |
|---------|------|
| View Admission Enquiries | Admin > Admission > Admission Enquiries |
| View Hostel Applications | Admin > Admission > Hostel Admissions |
| View Contact Messages | Admin > Contact > Contact Messages |
| Add Notices | Admin > Core > Notices |
| Upload Gallery Photos | Admin > Core > Gallery Images |
| Manage Programmes | Admin > Core > Programmes |

---

## 🎨 Design Features

- ✅ Fully responsive — Mobile, Tablet, Desktop
- ✅ Professional blue & gold nursing college theme
- ✅ Animated hero with floating logo
- ✅ Sticky navbar with active state
- ✅ Dynamic gallery with lightbox modal
- ✅ Tab-based admission form (Admission + Hostel)
- ✅ Accordion for college rules
- ✅ Google Maps embed
- ✅ Bootstrap 5 + Font Awesome icons
- ✅ Scroll reveal animations

---

## 🏗️ Django MVT Architecture

| Layer | Files |
|-------|-------|
| **Model** | `*/models.py` — Database tables for notices, gallery, admissions, contacts |
| **View** | `*/views.py` — Business logic, form handling |
| **Template** | `*/templates/**/*.html` — HTML pages |
| **URL** | `*/urls.py` — URL routing per app |
| **Admin** | `*/admin.py` — Admin panel config |

---

## 📞 College Contact

- **Phone:** +91 98390 64502
- **Email:** cmsnnursing@gmail.com
- **Address:** N.H. 28, Rudrapura Kushmi Kasia Road, Gorakhpur, UP 273002
- **Web:** www.cmsnnursingh.com

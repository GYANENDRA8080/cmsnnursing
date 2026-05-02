from django.shortcuts import render
from .models import Notice, GalleryImage, Programme


def home(request):
    notices = Notice.objects.filter(is_active=True)[:6]
    gallery = GalleryImage.objects.filter(is_active=True)[:12]
    programmes = Programme.objects.filter(is_active=True)
    context = {
        'notices': notices,
        'gallery': gallery,
        'programmes': programmes,
        'stats': {
            'students': '200+',
            'faculty': '20+',
            'programmes': '5+',
            'training': '100%',
        }
    }
    return render(request, 'core/home.html', context)


def gallery_view(request):
    gallery = GalleryImage.objects.filter(is_active=True)
    return render(request, 'core/gallery.html', {'gallery': gallery})

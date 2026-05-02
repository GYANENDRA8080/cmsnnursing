from django.db import models


class Notice(models.Model):
    title = models.CharField(max_length=300)
    link = models.URLField(blank=True, null=True)
    date_posted = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title


class Programme(models.Model):
    name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200)
    duration = models.CharField(max_length=50)
    intake = models.IntegerField()
    eligibility = models.TextField()
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

from django.db import models

class Movie(models.Model):
    STATUS_CHOICES = [
        ('watched', 'Watched'),
        ('to_watch', 'To Watch'),
    ]
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='to_watch')
    rating = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

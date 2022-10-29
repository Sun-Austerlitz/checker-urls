from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


class Url(models.Model):
    PAUSE_CHOICES = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='checking_urls')
    url = models.CharField(max_length=250)
    status_code = models.IntegerField(blank=True, null=True)
    interval = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)], help_text='in minutes')
    pause = models.CharField(max_length=3 ,choices=PAUSE_CHOICES, default='no')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('author', 'url',)
        ordering = ('-created',)

    def __str__(self):
        return self.url

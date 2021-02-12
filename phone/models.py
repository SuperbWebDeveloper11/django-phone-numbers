from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

class Phone(models.Model):
    office = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='phone_phone')

    def get_absolute_url(self):
        return reverse('phone:phone_detail', kwargs={'pk': self.pk})

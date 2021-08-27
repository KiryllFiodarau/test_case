from django.urls import reverse

from django.db import models


class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mail = models.EmailField(null=False, blank=False, unique=True)

    def __str__(self):
        return self.first_name+self.last_name

    def get_absolute_url(self):
        return reverse('get_user_by_id', kwargs={'user_id': self.pk})


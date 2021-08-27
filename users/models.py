from django.db import models


class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mail = models.EmailField(null=False, blank=False, unique=True)

    def __str__(self):
        return self.first_name+self.last_name

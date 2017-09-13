from __future__ import unicode_literals

from django.db import models

# Create your models here.
class test_job_app(models.Model):
    username = models.CharField(max_length=10, null=False)
    password = models.CharField(max_length=1o, null=False)
    objects = test_job_app_manager()
    def __str__(self):
    return self.test_job_name + ' & ' + self.app
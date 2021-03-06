from django.db import models
from django.urls import reverse

# Create your models here.
class CompanyModel(models.Model):
    name = models.CharField(max_length=50)
    ceo = models.CharField(max_length=30)
    location = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('company-detail', kwargs={'pk':self.pk})

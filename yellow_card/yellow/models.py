from django.db import models

# Create your models here.
from django.utils import timezone
import datetime
from datetime import datetime


class personal_details(models.Model):
    # pass
    immun = [
        ('YF ','Yellow Fever'),
        ('Ot','Others')
    ]
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    issue_date = models.DateTimeField(default=datetime.now)
    end_date = models.DateTimeField(default=datetime.now)
    immunised_for = models.CharField(max_length=45,choices=immun)
    passport_or_nin_number = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='pic')
    slug = models.SlugField(max_length=250,unique = True)
    
    def __str__(self):
        return self.passport_or_nin_number
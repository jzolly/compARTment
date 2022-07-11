from django.db import models

# Create your models here.
class Art(models.Model):
    name: models.CharField(max_length=100)
    mediums: models.CharField(max_length=150)
    description: models.CharField(max_length=250)
    date: models.DateField('Date Completed')
    img: models.CharField(max_length=250)

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.
class pouzivatel(models.Model):
    fname = models.CharField(max_length=40, null=False, blank=False)


class booking(models.Model):
    Ffname = models.CharField(max_length=100)
    Femail = models.EmailField()
    Fdate = models.DateField()
    Fpoznamka = models.TextField(blank=True)
    Foption = models.CharField(max_length=50)
    
    def __str__(self):
        return self.Ffname

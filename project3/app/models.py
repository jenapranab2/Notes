from django.db import models

# Create your models here.
class Notes(models.Model):
    sln = models.IntegerField(primary_key=True)
    name =models.CharField(max_length=50)
    un = models.CharField(max_length=50)
    pw = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Notec(models.Model):
    sln =models.IntegerField(null=True)
    title = models.CharField(null=True, max_length=50)
    desc = models.CharField(null=True, max_length=50)

    def __str__(self):
        return self.title
from django.db import models

# Create your models here.
class Info(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    logo = models.ImageField(upload_to='info/')
    facebook = models.URLField()
    instagram = models.URLField()
    twitter = models.URLField()

    def __str__(self):
        return self.email
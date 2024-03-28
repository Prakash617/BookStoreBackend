from django.db import models

# Create your models here.

class Carousal(models.Model):
    title = models.CharField(max_length=9999,null=True,blank=True)
    subtitle = models.CharField(max_length=9999,null=True,blank=True)
    link = models.URLField(null=True,blank=True)
    image = models.ImageField(upload_to='carousel_images/')
    link_text = models.CharField(max_length=999999,null=True,blank=True)

    def __str__(self):
        return self.title


class Faqs(models.Model):
    question = models.CharField(max_length=99999)
    answer = models.TextField()

    def __str__(self):
        return self.question


class Menus(models.Model):
    name = models.CharField(max_length=9999)
    url = models.CharField(max_length=9999)

    def __str__(self):
        return self.name

class Careers(models.Model):
    title = models.CharField(max_length=9999)
    created_at = models.DateField(auto_now_add=True)
    description = models.TimeField()
    image = models.ImageField(upload_to='careers_images/')
    quantity = models.IntegerField()

    def __str__(self):
        return self.title










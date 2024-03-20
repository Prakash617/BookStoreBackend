from django.db import models


Language = (
        ('Nepali', 'Nepali'),
        ('English', 'English'),
       
    )

class Category(models.Model):
    name = models.CharField(max_length=9999)
    slug = models.CharField(max_length=9999,unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=9999)
    author = models.CharField(max_length=9999)
    description = models.TextField()
    price = models.FloatField()
    published_date = models.DateField(null=True,blank=True)
    edition = models.CharField(null=True,blank=True)
    page_count = models.IntegerField(null=True,blank=True)
    isbn_number = models.CharField(null=True,blank=True)
    language = models.CharField(choices=Language,default="English")
    top_selling = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=True)
    new_arrival = models.BooleanField(default=True)

    def __str__(self):
        return self.title

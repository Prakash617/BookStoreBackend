from django.db import models
from user_accounts.models import CustomUser
from django.utils.text import slugify


Language = (
        ('Nepali', 'Nepali'),
        ('English', 'English'),
       
    )
Stockchoice = (
    ('In stock', 'In stock'),
    ('Out of Stock', 'Out of Stock')
)

coupon_types = (
    ('Percentage Discount', 'Percentage Discount'),
    ('Flat Discount', 'Flat Discount'),
    ('Bulk Discount', 'Bulk Discount'),
    ('Free Shipping', 'Free Shipping'),
)
def default_coupon_details():
    return {"empty": "empty"}


class Category(models.Model):
    name = models.CharField(max_length=9999)
    slug = models.CharField(max_length=9999,unique=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
class SubCategory(models.Model):
    name = models.CharField(max_length=9999)
    sub_slug = models.CharField(max_length=9999,unique=True,null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.sub_slug:
            self.sub_slug = slugify(self.name)
        super().save(*args, **kwargs)
class Author(models.Model):
    name = models.CharField(max_length=999)
    slug = models.CharField(max_length=9999,unique=True,blank=True)
    bio = models.TextField()
    image = models.FileField(upload_to='authors/',blank=True, default="author/profile.jpg")
    nationality = models.CharField(max_length=99999,null=True,blank=True)
    is_bestseller = models.BooleanField(default=False)


    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)




class Coupon(models.Model):
    name=models.CharField(max_length=400)
    coupon_types=models.CharField(max_length=400,choices=coupon_types,default="Percentage Discount")
    coupon_details=models.JSONField(default=default_coupon_details,null=True,blank=True)

    def __str__(self):
        return self.name
    


class Book(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True)    
    title = models.CharField(max_length=9999)
    authors = models.ManyToManyField(Author, related_name='products')
    description = models.TextField()
    product_image  =  models.FileField(upload_to='product/',blank=True, default="product/Product.jpg")
    SKU = models.CharField(max_length=9999,null=True,blank=True)
    stock_status = models.CharField(choices=Stockchoice,default="In Stock", max_length=9999, blank=True, null=True)
    stock_quantity = models.IntegerField(default=1)
    sell_quantity = models.IntegerField(default=0)
    price = models.FloatField()
    published_date = models.DateField(null=True,blank=True)
    edition = models.CharField(max_length=9999,null=True,blank=True)
    page_count = models.IntegerField(null=True,blank=True)
    isbn_number = models.CharField(max_length=9999,null=True,blank=True)
    language = models.CharField(max_length=9999,choices=Language,default="English")
    top_selling = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=True)
    new_arrival = models.BooleanField(default=True)
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.stock_quantity == self.sell_quantity:
            self.stock_status = "Out of Stock"
        # Call the original save method
        super(Book, self).save(*args, **kwargs)


class Tag(models.Model):
    product = models.ManyToManyField(Book)
    tag = models.CharField(max_length=75 ,unique=True)
    
    def __str__(self):
        return self.tag
    
class Review(models.Model):
    product = models.ForeignKey(Book,related_name='review_product',null=True, blank=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(CustomUser, related_name='reviewing_customer', on_delete=models.CASCADE)
    star_count = models.IntegerField()
    review_text = models.CharField(max_length=400)
    
    def __str__(self):
        return self.product.title
    
class ProductQueries(models.Model):
    product = models.ForeignKey(Book,related_name='query_product',null=True, blank=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(CustomUser, related_name='query_customer', on_delete=models.CASCADE)
    question = models.CharField(max_length=999)
    answer = models.CharField(max_length=999)
    
    def __str__(self):
        return self.question
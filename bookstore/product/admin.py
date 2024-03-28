from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(SubCategory)
admin.site.register(Coupon)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Review)
admin.site.register(ProductQueries)
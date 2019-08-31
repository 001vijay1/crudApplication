from django.contrib import admin
from .models import Book,BookProfile,Contact

# Register your models here.
admin.site.register(Book)
admin.site.register(BookProfile)
admin.site.register(Contact)

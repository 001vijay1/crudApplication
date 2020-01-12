from django.contrib import admin
from .models import Book,BookProfile,Contact
from django.contrib.admin.options import ModelAdmin

# Register your models here.
class BookAdmin(ModelAdmin):
    list_display = ['book_name','publish_date']
    search_fields = ['book_name']

admin.site.register(Book,BookAdmin)
admin.site.register(BookProfile)
admin.site.register(Contact)



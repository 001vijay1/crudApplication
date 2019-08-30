from django.db import models
from django.db.models.signals import post_save

# Create your models here.
class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=50)
    auther_name = models.CharField(max_length=30)
    price = models.IntegerField()



    def __str__(self):
        return self.book_name

class BookProfile(models.Model):
    book = models.OneToOneField(Book,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="book/images",default="")
    desc = models.TextField(max_length=200)

    def __str__(self):
        return self.book.book_name

def save_profile(sender, instance, **kwargs):
    BookProfile.objects.create(book=instance)
post_save.connect(save_profile, sender=Book)

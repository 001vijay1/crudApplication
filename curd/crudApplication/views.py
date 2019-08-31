from django.shortcuts import render,redirect
from .forms import AddBookForm
from .models import Book,BookProfile,Contact

# Create your views here.
def add_book(request):
    form= AddBookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('show')
    return render(request,'add_book.html',{'form':form})

def show_book(request):
    form =Book.objects.all()
    return render(request,'show_books.html',{'form':form})

def delete_book(request, book_id):
    form = Book.objects.get(book_id=book_id)
    form.delete()
    return redirect("show")
def edit_record(request, book_id):
    form = Book.objects.get(book_id=book_id)
    return render(request, 'edit.html', {'form': form})

def update_record(request, book_id):
    record = Book.objects.get(book_id=book_id)
    form = AddBookForm(request.POST or None, instance=record)
    if(form.is_valid()):
        form.save()
        return redirect('show')
    return render(request, 'edit.html')

def profile(request,book_id):
    form = BookProfile.objects.get(book_id=book_id)
    return render(request, 'profile.html', {'form': form})

def contact(request):
    thanks = False
    if (request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thanks = True
    return render(request , 'contact.html',{'thanks':thanks})
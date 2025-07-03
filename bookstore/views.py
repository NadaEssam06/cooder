from django.shortcuts import redirect, render
from django.http import HttpResponse
from bookstore.models import Books
from bookstore.forms import BookForm
from django.conf import settings
# Create your views here.
def index(request):
    # res=HttpResponse("Hi from book store")
    # res['Content-Type']= 'text/palin'
    # return res
    return render(request,'base_layout.html')
def book_list(request):
    all_books= Books.objects.all()
    print(all_books)
    return render(request,'book_list.django-html',context={
        "books":all_books,
        "MEDIA_URL": settings.MEDIA_URL})


def book_detail(request,isbn):
    book= Books.objects.get(ISBN=isbn)
    return render(request,"book_details.django-html",context={
        "book":book, 
        "MEDIA_URL": settings.MEDIA_URL})

def book_create (request):
    form= BookForm()
    if request.method == "POST":
        form=BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("bookstore:bookstore-index")
    return render(request,"book_create.django-html",context={
        "form":form,
        "MEDIA_URL": settings.MEDIA_URL})

def book_update(request,isbn):
    book= Books.objects.get(ISBN=isbn)
    form=BookForm(instance=book)
    if request.method== "POST":
        form=BookForm(request.POST,request.FILES,instance=book)
        if form.is_valid():
            form.save()
            return redirect("bookstore:bookstore-book_detail",isbn=book.ISBN)
    return render(request,"book_update.django-html",context={
        "form":form,
        "book":book})

def book_delete(request,isbn):
    Books.objects.get(ISBN=isbn).delete()
    return redirect("bookstore:bookstore-index")




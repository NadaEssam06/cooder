from django.shortcuts import redirect, render
from django.http import HttpResponse
# Create your views here.
def index(request):
    # res=HttpResponse("Hi from book store")
    # res['Content-Type']= 'text/palin'
    # return res
    return render(request,'base_layout.html')
def book_list(request):
    my_context={
        'book_list':books
    }
    return render(request,'book_list.django-html',context=my_context)
def _get_book_by_isbn(isbn):
    for book in books:
        if isbn ==book['ISBN']:
            return book
    return None

def book_detail(request,*args,**kwargs):
    book_id=kwargs.get('book_id')
    mycontext={}
    mycontext['book']=_get_book_by_isbn(book_id)
    return render(request,"book_details.django-html",context=mycontext)

def book_update(request,*args,**kwargs):
    book_id=kwargs.get('book_id')
    mycontext={}
    mycontext['book']=_get_book_by_isbn(book_id)
    if mycontext["book"]:
        mycontext["book"]['title']=f"updated {mycontext["book"]['title']}"
    return redirect("bookstore:bookstore-index")

def book_delete(request,*args,**kwargs):
    book_id=kwargs.get('book_id')
    mycontext={}
    mycontext['book']=_get_book_by_isbn(book_id)
    if mycontext["book"]:
        books.remove(mycontext["book"])
    return redirect("bookstore:bookstore-index")


books = [
    {"ISBN":1,
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt & David Thomas",
        "price": 39.99,
        "image": "pragmatic_programmer.jpg",
        "description": "A classic guide for software developers on how to think and code like a professional.",
    },
    {"ISBN":2,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "price": 34.99,
        "image": "clean_code.jpg",
        "description": "Learn how to write clean, maintainable, and efficient code in any language.",
    },
    {"ISBN":3,
        "title": "Atomic Habits",
        "author": "James Clear",
        "price": 24.50,
        "image": "atomic_habits.jpg",
        "description": "Build good habits, break bad ones, and master tiny behaviors that lead to success.",
    },
    {"ISBN":4,
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "price": 29.99,
        "image": "python_crash_course.jpg",
        "description": "A hands-on, project-based introduction to programming in Python.",
    },
    {"ISBN":5,
        "title": "Deep Work",
        "author": "Cal Newport",
        "price": 21.00,
        "image": "deep_work.jpg",
        "description": "Rules for focused success in a distracted world — boost productivity and concentration.",
    },
]

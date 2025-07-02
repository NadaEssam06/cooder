from django.urls import include, path
from .views import index,book_list,book_detail,book_update,book_delete
app_name='bookstore'
urlpatterns = [
    # path('index',index,name='bookstore-index'),
    path('index',book_list,name='bookstore-index'),
    path('book/<int:book_id>',book_detail,name='bookstore-book_detail'),
    path('book_update/<int:book_id>',book_update,name='bookstore-book_update'),
    path('book_delete/<int:book_id>',book_delete,name='bookstore-book_delete'),
]

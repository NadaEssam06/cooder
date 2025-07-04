from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static
from .views import index,book_list,book_detail,book_update,book_delete, book_create
app_name='bookstore'
urlpatterns = [
    # path('index',index,name='bookstore-index'),
    path('index',book_list,name='bookstore-index'),
    path('book/<uuid:isbn>',book_detail,name='bookstore-book_detail'),
    path('book_update/<uuid:isbn>',book_update,name='bookstore-book_update'),
    path('book_create',book_create,name='bookstore-book_create'),
    path('book_delete/<uuid:isbn>',book_delete,name='bookstore-book_delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

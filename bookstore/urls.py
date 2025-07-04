from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static
from .views import index,book_list,book_detail,book_update,book_delete, book_create
from django.views.decorators.csrf import csrf_exempt
app_name='bookstore'
urlpatterns = [
    # path('index',index,name='bookstore-index'),
    path('index',book_list,name='bookstore-index'),
    path('book/<int:id>',book_detail,name='bookstore-book_detail'),
    path('book_update/<int:id>',book_update,name='bookstore-book_update'),
    path('book_create',book_create,name='bookstore-book_create'),
    path('book_delete/<int:id>',book_delete,name='bookstore-book_delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

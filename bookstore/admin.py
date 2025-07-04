from django.contrib import admin
from .models import Books, Categories, ISBN
# Register your models here.
class bookAdmin(admin.ModelAdmin):
    list_filter=('author','price','created_at')
    search_fields=('author','isbn')
    fieldsets=(
        ["Main info",{
            "fields":["isbn","title","author"]
        }]
    )

admin.site.register(Books)
admin.site.register(Categories)
admin.site.register(ISBN)
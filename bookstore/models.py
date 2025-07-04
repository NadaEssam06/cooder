from datetime import timezone
import uuid
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categories(models.Model):
    name= models.CharField(max_length=70)
    def __str__(self):
        return self.name
    class Meta:
        db_table="Categories"

class ISBN (models.Model):
    isbn = models.UUIDField(default=uuid.uuid4, unique=True)

    def __str__(self):
        return str( self.isbn)
 
    @property
    def book_title(self):
        return self.book.title
    @property
    def author_title(self):
        return self.book.author.username

    class Meta:
        db_table="ISBN"
        
class Books(models.Model):
    isbn=models.OneToOneField("ISBN", on_delete=models.CASCADE,related_name='book', default=uuid.uuid4)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="authored_book")
    title=models.CharField("Book Title",max_length=255,unique=True)
    price=models.PositiveIntegerField("Bool Price",default=0)
    image=models.ImageField("Book cover",upload_to='images/',blank=True)
    categories=models.ManyToManyField("Categories",related_name='books')
    description=models.CharField("Book Description",max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Title: {self.title}"
    class Meta:
        db_table= "Books"

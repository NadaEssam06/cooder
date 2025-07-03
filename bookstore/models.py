from django.db import models

# Create your models here.
class Books(models.Model):
    ISBN= models.CharField("ISBN",max_length=255,unique=True)
    title=models.CharField("Book Title",max_length=255,unique=True)
    author=models.CharField("Author",max_length=255)
    price=models.PositiveIntegerField("Bool Price",default=0)
    image=models.ImageField("Book cover",upload_to='images/',blank=True)
    description=models.CharField("Book Description",max_length=255)
    def __str__(self):
        return f"Title: {self.title}"
    class Meta:
        db_table= "Books"
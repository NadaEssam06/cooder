from django.forms import ModelForm
from bookstore.models import Books

class BookForm(ModelForm):
    def __init__(self,*args, **kwargs):
        super(BookForm,self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'bg-gray-800 text-gray-100 border border-gray-700 rounded px-4 py-2 w-full'
            })
    class Meta:
        model= Books
        fields="__all__"

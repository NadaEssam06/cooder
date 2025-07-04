from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class':"w-full px-4 py-2 rounded-lg bg-gray-800 border border-indigo-600 focus:outline-none focus:ring-2 focus:ring-indigo-500 shadow-sm" 
            })
    class Meta:
        model = User
        fields = ('username', 'email','first_name', 'last_name', 'password1', 'password2')
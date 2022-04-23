from django import forms
from .models import User

class NameForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['name', 'surname', 'email_address', 'password']
        # This widget solves only the type of the field not the security!
        widgets = {
          'password': forms.PasswordInput(),
        }

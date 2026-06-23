from django import forms
from .models import FoundItem, LostItem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User  # Specify the model as User here
        fields = ['username', 'email', 'password1', 'password2']  # These fields come from UserCreationForm
        
def save(self, commit=True):
    user = super().save(commit=False)
    user.email = self.cleaned_data['email']
    if commit:
        user.save()
    return user


class FoundItemForm(forms.ModelForm):
    class Meta:
        model = FoundItem
        fields = ['item_name', 'description', 'location', 'date']


class LostItemForm(forms.ModelForm):
    class Meta:
        model = LostItem
        fields = ['item_name', 'description', 'location', 'date']

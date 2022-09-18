from django import forms
from .models import  Profile,Post

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'avatar')
    


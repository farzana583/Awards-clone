from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import  Profile, Image
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username','email','password1','password2']


class SignUpForm(UserCreationForm):
    email = forms.EmailField(help_text='Enter Email!')  
    
                               
class NewPostForm(forms.ModelForm):
    '''
    Form for a user to create a new form
    '''
    class Meta:
        model = Image
        exclude = ['image_poster']
  
class ProfileUpdateForm(forms.ModelForm):
      class Meta:
          model = Profile
          fields = ['image']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    bio = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email','bio']
from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    # name = forms.CharField(max_length=255)
    # imgName = forms.ImageField()

    class Meta:
        model = Image
        fields = ('name','imgSrc')


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    # no email in default usercreationform so adding 
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name', 'password1','password2']
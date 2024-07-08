from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    # name = forms.CharField(max_length=255)
    # imgName = forms.ImageField()

    class Meta:
        model = Image
        fields = ('name','imgSrc')
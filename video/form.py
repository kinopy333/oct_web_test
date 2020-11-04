from django import forms
from .models import Video, Review

class VideoModelForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('title', 'videofile',)

class RevieModelForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('name', 'body')
        widgets = {
            'body' : forms.RadioSelect()
        }


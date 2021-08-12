from django.db.models.base import Model
from django.forms import ModelForm, widgets
from django import forms
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'featured_image', 'description','tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
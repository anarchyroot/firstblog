from datetime import timezone

from django import forms
from flask import request

from .models import Post


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image')

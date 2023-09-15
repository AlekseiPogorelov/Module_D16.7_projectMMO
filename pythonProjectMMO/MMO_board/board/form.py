from django import forms

from .models import Post, UserResponse


class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = [
           'user',
           'subject',
           'category',
           'text',
       ]


class UserResponseForm(forms.ModelForm):
   class Meta:
       model = UserResponse
       fields = [
           'user',
           'subject',
           'text',
           'post',
       ]
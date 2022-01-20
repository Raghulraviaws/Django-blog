from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Post,Comment 




class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'title', 'text')

        widgets = {

            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text' :forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})


        }

class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text')

        widgets = {

            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})

        }


# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#
#     class Meta():
#         model = User
#         fields = ('username', 'email', 'password')
#
# class UserProfileInfoForm(forms.ModelForm):
#     class Meta():
#         model = UserProfileInfo
#         fields = ('profile_pic', 'portfolio_site')

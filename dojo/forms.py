from django import forms
from dojo.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

    # def save(self, commit=True):
    #     self.instance = Post(**self.cleaned_data)
    #     if commit:
    #         self.instance.save()
    #         return post
    #



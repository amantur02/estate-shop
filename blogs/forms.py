from blogs.models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )


class PostCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category', 'title', 'heading', 'text', 'image')


# class PostUpdate(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ('')
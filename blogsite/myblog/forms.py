from django import forms
from .models import Post, Category, Tag

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'tags']  # Exclude 'author' and 'publish_date' as they are set automatically

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # Get the current user from the kwargs
        super().__init__(*args, **kwargs)

        # Limit categories and tags choices 
        self.fields['category'].queryset = Category.objects.all()
        self.fields['tags'].queryset = Tag.objects.all()

        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'rows': 20})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['tags'].widget.attrs.update({'class': 'form-control', 'multiple': 'multiple'})

    def save(self, commit=True):
        post = super().save(commit=False)
        if self.user:
            post.author = self.user  # Set the author to the current user
        if commit:
            post.save()
            self.save_m2m()  # Save the many-to-many field
        return post
from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body', 'image']

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size >= 5 * 1024 * 1024:
                raise forms.ValidationError('Fayl hajmi 5 MB dan oshmasligi kerak.')
        return image

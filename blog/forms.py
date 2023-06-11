from .models import Recipe, Comment
from django import forms
from django_summernote.widgets import SummernoteWidget


class RecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget = forms.Textarea(attrs={'rows': 2})

    class Meta:
        model = Recipe
        fields = [
            'title',
            'featured_image',
            'description',
            'ingredients',
            'preparing_time',
            'cooking_time',
            'serves',
            'difficulty',
            'category',
            'method',
            'status',
        ]
        widgets = {
            'method': SummernoteWidget(),
            'ingredients': SummernoteWidget(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

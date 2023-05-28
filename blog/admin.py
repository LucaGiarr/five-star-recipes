from django.contrib import admin
from .models import UserProfile, Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):

    list_display = ('user',)


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('title', 'category', 'slug', 'status',
                    'created_on')
    search_fields = ['title', 'method']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('category', 'status', 'created_on')
    summernote_fields = ('description','ingredients', 'method')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'recipe', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

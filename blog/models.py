from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField


STATUS = ((0, "Draft"), (1, "Published"))
CATEGORY = ((0, "Starter"), (1, "Main Course"),
            (2, "Dessert"), (3, "Other"))


class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_recipes"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    website = models.TextField(blank=True)
    website_url = models.URLField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    ingredients = models.TextField(blank=True)
    preparing_time = models.CharField(max_length=200, default='10 mins')
    cooking_time = models.CharField(max_length=200, default='10 mins')
    serves = models.IntegerField(default=2)
    difficulty = models.CharField(max_length=200, default='Easy')
    category = models.IntegerField(choices=CATEGORY, default=1)
    updated_on = models.DateTimeField(auto_now=True)
    method = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogrecipe_like', blank=True)
    favourites = models.ManyToManyField(
        User, related_name='blogrecipe_favourite', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def get_absolute_url(self):
        return reverse('recipe_details',  kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def approved_comments(self):
        return self.comments.filter(approved=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

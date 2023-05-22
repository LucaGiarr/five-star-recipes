# Generated by Django 3.2.19 on 2023-05-21 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_delete_recipeofday'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeOfDay',
            fields=[
                ('recipe_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.recipe')),
            ],
            options={
                'ordering': ['category'],
            },
            bases=('blog.recipe',),
        ),
    ]
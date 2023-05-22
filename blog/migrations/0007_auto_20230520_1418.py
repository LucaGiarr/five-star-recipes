# Generated by Django 3.2.19 on 2023-05-20 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_recipe_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='recipe',
            name='receipe_of_day',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], default=0),
        ),
    ]
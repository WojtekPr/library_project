# Generated by Django 4.2.1 on 2023-06-20 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_book_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='reserved',
            field=models.BooleanField(default=False),
        ),
    ]
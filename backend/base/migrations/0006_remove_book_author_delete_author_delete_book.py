# Generated by Django 4.2.4 on 2025-02-15 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_author_alter_book_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]

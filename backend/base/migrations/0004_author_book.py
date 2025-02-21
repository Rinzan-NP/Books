# Generated by Django 4.2.4 on 2025-02-15 19:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rename_is_superadmin_account_is_superuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(blank=True, max_length=10)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('fans_count', models.IntegerField(default=0)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('work_id', models.CharField(max_length=100, unique=True)),
                ('isbn', models.CharField(blank=True, max_length=20, null=True)),
                ('isbn13', models.CharField(blank=True, max_length=20, null=True)),
                ('asin', models.CharField(blank=True, max_length=20, null=True)),
                ('language', models.CharField(blank=True, max_length=10, null=True)),
                ('average_rating', models.FloatField(default=0)),
                ('rating_dist', models.TextField(blank=True, null=True)),
                ('ratings_count', models.IntegerField(default=0)),
                ('text_reviews_count', models.IntegerField(default=0)),
                ('publication_date', models.DateField(blank=True, null=True)),
                ('original_publication_date', models.DateField(blank=True, null=True)),
                ('format', models.CharField(blank=True, max_length=50, null=True)),
                ('edition_information', models.CharField(blank=True, max_length=255, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('publisher', models.CharField(blank=True, max_length=255, null=True)),
                ('num_pages', models.IntegerField(blank=True, null=True)),
                ('series_id', models.CharField(blank=True, max_length=100, null=True)),
                ('series_name', models.CharField(blank=True, max_length=255, null=True)),
                ('series_position', models.IntegerField(blank=True, null=True)),
                ('authors', models.ManyToManyField(related_name='books', to='base.author')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

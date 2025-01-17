# Generated by Django 5.0.1 on 2024-01-03 19:31

import django.contrib.gis.db.models.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('backend', '0002_remove_pla_categories_delete_cit_delete_cate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(help_text='Specify a cultural heritage category', max_length=50, verbose_name='Category name')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(default='station')),
                ('point_geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Locations',
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=50, verbose_name='Place name')),
                ('color', models.CharField(default='green', max_length=50, verbose_name='Place Color')),
                ('description', models.TextField(blank=True, verbose_name='Place description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='place_images/')),
                ('active', models.BooleanField(default=True)),
                ('point_geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.category')),
            ],
            options={
                'verbose_name_plural': 'Places',
            },
        ),
    ]

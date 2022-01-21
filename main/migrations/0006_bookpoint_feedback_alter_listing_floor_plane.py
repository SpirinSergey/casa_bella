# Generated by Django 4.0 on 2022-01-17 15:54

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_listing_unit_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='Last name')),
                ('phone', models.CharField(blank=True, max_length=150, verbose_name='Phone')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('date', models.CharField(blank=True, max_length=50, verbose_name='Date and time')),
                ('date_creation', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date creation')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Book an appointments',
            },
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='Last name')),
                ('phone', models.CharField(blank=True, max_length=150, verbose_name='Phone')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('date_creation', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date creation')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Feedbacks',
            },
        ),
        migrations.AlterField(
            model_name='listing',
            name='FLOOR_PLANE',
            field=models.FileField(blank=True, upload_to=main.models.floor_plane),
        ),
    ]

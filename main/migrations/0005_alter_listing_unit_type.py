# Generated by Django 4.0 on 2021-12-22 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_listing_floor_plane_alter_listing_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='UNIT_TYPE',
            field=models.CharField(max_length=20, null=True),
        ),
    ]

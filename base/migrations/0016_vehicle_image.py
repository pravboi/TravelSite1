# Generated by Django 3.2.8 on 2023-03-18 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_expedition_avalible'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

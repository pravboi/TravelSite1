# Generated by Django 3.2.8 on 2023-03-17 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_auto_20230317_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='expedition',
            name='avalible',
            field=models.BooleanField(default=True, null=True),
        ),
    ]

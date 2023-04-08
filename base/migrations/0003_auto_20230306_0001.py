# Generated by Django 3.2.8 on 2023-03-06 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_vehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='description',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='recovery_description',
            field=models.CharField(max_length=5000, null=True),
        ),
    ]

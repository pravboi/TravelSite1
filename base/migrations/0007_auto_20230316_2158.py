# Generated by Django 3.2.8 on 2023-03-16 21:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20230306_0125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passenger', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='passenger', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='currentvehicle',
            name='seats',
            field=models.ManyToManyField(blank=True, related_name='seats', to='base.Seat'),
        ),
    ]

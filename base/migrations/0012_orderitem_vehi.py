# Generated by Django 3.2.8 on 2023-03-17 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_orderitem_exp'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='vehi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehi', to='base.vehicle'),
        ),
    ]

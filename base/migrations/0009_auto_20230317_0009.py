# Generated by Django 3.2.8 on 2023-03-17 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20230316_2219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='vehicle',
        ),
        migrations.AddField(
            model_name='ticket',
            name='exped',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='exped', to='base.expedition'),
        ),
    ]
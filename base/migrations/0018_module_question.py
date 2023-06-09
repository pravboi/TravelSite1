# Generated by Django 3.2.8 on 2023-03-18 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_remove_vehicle_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prompt', models.CharField(max_length=100, null=True)),
                ('choice1', models.CharField(max_length=100, null=True)),
                ('choice2', models.CharField(max_length=100, null=True)),
                ('choice3', models.CharField(max_length=100, null=True)),
                ('choice4', models.CharField(max_length=100, null=True)),
                ('answer', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('questions', models.ManyToManyField(blank=True, related_name='questions', to='base.Question')),
            ],
        ),
    ]

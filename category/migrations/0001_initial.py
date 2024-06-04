# Generated by Django 5.0.6 on 2024-06-04 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=100)),
                ('tasks', models.ManyToManyField(related_name='categories', to='task.taskmodel')),
            ],
        ),
    ]

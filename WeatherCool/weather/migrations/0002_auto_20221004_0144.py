# Generated by Django 3.1.4 on 2022-10-03 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-31 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fromapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=254),
        ),
    ]

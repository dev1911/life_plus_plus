# Generated by Django 2.2.3 on 2019-09-02 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prescription', '0005_auto_20190831_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescriptions',
            name='text',
            field=models.TextField(default=''),
        ),
    ]

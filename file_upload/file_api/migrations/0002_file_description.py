# Generated by Django 5.0.2 on 2024-02-11 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='description',
            field=models.CharField(default='no description available', max_length=160),
            preserve_default=False,
        ),
    ]
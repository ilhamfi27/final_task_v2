# Generated by Django 3.0.3 on 2020-06-16 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0009_datasetprofile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasetprofile',
            name='type',
            field=models.CharField(default='', max_length=50),
        ),
    ]

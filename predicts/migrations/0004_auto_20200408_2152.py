# Generated by Django 3.0.3 on 2020-04-08 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predicts', '0003_auto_20200328_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='prediction',
            name='dumped_model',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='prediction',
            name='feature_num',
            field=models.IntegerField(default=0, max_length=3),
        ),
        migrations.AddField(
            model_name='prediction',
            name='ranked_index',
            field=models.CharField(default='', max_length=255),
        ),
    ]

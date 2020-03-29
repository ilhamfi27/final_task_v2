# Generated by Django 3.0.3 on 2020-03-28 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0002_city_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='BPS_poverty_rate',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='avg_buyer_apt_rent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='avg_buyer_apt_sell',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='avg_buyer_car',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='avg_buyer_land_rent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='avg_buyer_land_sell',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='avg_buyer_motor',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='avg_buyer_rumah_rent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='avg_buyer_rumah_sell',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='avg_price_apt_rent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='avg_price_apt_sell',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='avg_price_car',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='avg_price_land_rent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='avg_price_land_sell',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='avg_price_motor',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='avg_price_rumah_rent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='avg_price_rumah_sell',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='avg_sold_apt_rent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='avg_sold_apt_sell',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='avg_sold_car',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='avg_sold_land_rent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='avg_sold_land_sell',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='avg_sold_motor',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='avg_sold_rumah_rent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='avg_sold_rumah_sell',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='avg_viewer_apt_rent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='avg_viewer_apt_sell',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='avg_viewer_car',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='avg_viewer_land_rent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='avg_viewer_land_sell',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='avg_viewer_motor',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='avg_viewer_rumah_rent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='avg_viewer_rumah_sell',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='std_buyer_apt_rent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='std_buyer_apt_sell',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='std_buyer_car',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='std_buyer_land_rent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='std_buyer_land_sell',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='std_buyer_motor',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='std_buyer_rumah_rent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='std_buyer_rumah_sell',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='std_price_apt_rent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='std_price_apt_sell',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='std_price_car',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='std_price_land_rent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='std_price_land_sell',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='std_price_motor',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='std_price_rumah_rent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='std_price_rumah_sell',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='std_sold_apt_rent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='std_sold_apt_sell',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='std_sold_car',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='std_sold_land_rent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='std_sold_land_sell',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='std_sold_motor',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='std_sold_rumah_rent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='std_sold_rumah_sell',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='std_viewer_apt_rent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='std_viewer_apt_sell',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='std_viewer_car',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='std_viewer_land_rent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='std_viewer_land_sell',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='std_viewer_motor',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='std_viewer_rumah_rent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='std_viewer_rumah_sell',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='sum_buyer_apt_rent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='sum_buyer_apt_sell',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='sum_buyer_car',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='sum_buyer_land_rent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='sum_buyer_land_sell',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='sum_buyer_motor',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='sum_buyer_rumah_rent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='sum_buyer_rumah_sell',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='sum_price_apt_rent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='sum_price_apt_sell',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='sum_price_car',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='sum_price_land_rent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='sum_price_land_sell',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='sum_price_motor',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='sum_price_rumah_rent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='sum_price_rumah_sell',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='sum_sold_apt_rent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='sum_sold_apt_sell',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='sum_sold_car',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='sum_sold_land_rent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='sum_sold_land_sell',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='sum_sold_motor',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='sum_sold_rumah_rent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='sum_sold_rumah_sell',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='sum_viewer_apt_rent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='sum_viewer_apt_sell',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='sum_viewer_car',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='sum_viewer_land_rent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='sum_viewer_land_sell',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='sum_viewer_motor',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='sum_viewer_rumah_rent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='sum_viewer_rumah_sell',
            field=models.FloatField(default=0),
        ),
    ]
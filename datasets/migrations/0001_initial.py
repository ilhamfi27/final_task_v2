# Generated by Django 3.0.3 on 2020-03-11 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('latitude', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('province', models.CharField(default='', max_length=40)),
            ],
            options={
                'db_table': 'cities',
            },
        ),
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BPS_poverty_rate', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('sum_price_car', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('avg_price_car', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('std_price_car', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('sum_sold_car', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('avg_sold_car', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('std_sold_car', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('sum_viewer_car', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('avg_viewer_car', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('std_viewer_car', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('sum_buyer_car', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('avg_buyer_car', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('std_buyer_car', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('sum_price_motor', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('avg_price_motor', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('std_price_motor', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('sum_sold_motor', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('avg_sold_motor', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('std_sold_motor', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('sum_viewer_motor', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('avg_viewer_motor', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('std_viewer_motor', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('sum_buyer_motor', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('avg_buyer_motor', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('std_buyer_motor', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('sum_price_rumah_sell', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('avg_price_rumah_sell', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('std_price_rumah_sell', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('sum_sold_rumah_sell', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('avg_sold_rumah_sell', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('std_sold_rumah_sell', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('sum_viewer_rumah_sell', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('avg_viewer_rumah_sell', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('std_viewer_rumah_sell', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('sum_buyer_rumah_sell', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('avg_buyer_rumah_sell', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('std_buyer_rumah_sell', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('sum_price_rumah_rent', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('avg_price_rumah_rent', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('std_price_rumah_rent', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('sum_sold_rumah_rent', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('avg_sold_rumah_rent', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('std_sold_rumah_rent', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('sum_viewer_rumah_rent', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('avg_viewer_rumah_rent', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('std_viewer_rumah_rent', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('sum_buyer_rumah_rent', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('avg_buyer_rumah_rent', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('std_buyer_rumah_rent', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('sum_price_apt_sell', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('avg_price_apt_sell', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('std_price_apt_sell', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('sum_sold_apt_sell', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('avg_sold_apt_sell', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('std_sold_apt_sell', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('sum_viewer_apt_sell', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('avg_viewer_apt_sell', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('std_viewer_apt_sell', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('sum_buyer_apt_sell', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('avg_buyer_apt_sell', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('std_buyer_apt_sell', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('sum_price_apt_rent', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('avg_price_apt_rent', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('std_price_apt_rent', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('sum_sold_apt_rent', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('avg_sold_apt_rent', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('std_sold_apt_rent', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('sum_viewer_apt_rent', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('avg_viewer_apt_rent', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('std_viewer_apt_rent', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('sum_buyer_apt_rent', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('avg_buyer_apt_rent', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('std_buyer_apt_rent', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('sum_price_land_sell', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('avg_price_land_sell', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('std_price_land_sell', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('sum_sold_land_sell', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('avg_sold_land_sell', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('std_sold_land_sell', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('sum_viewer_land_sell', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('avg_viewer_land_sell', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('std_viewer_land_sell', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('sum_buyer_land_sell', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('avg_buyer_land_sell', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('std_buyer_land_sell', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('sum_price_land_rent', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('avg_price_land_rent', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('std_price_land_rent', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('sum_sold_land_rent', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('avg_sold_land_rent', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('std_sold_land_rent', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('sum_viewer_land_rent', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('avg_viewer_land_rent', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('std_viewer_land_rent', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('sum_buyer_land_rent', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('avg_buyer_land_rent', models.DecimalField(decimal_places=7, default=0, max_digits=25)),
                ('std_buyer_land_rent', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datasets.City')),
            ],
            options={
                'db_table': 'ecommerce_transactions',
            },
        ),
    ]

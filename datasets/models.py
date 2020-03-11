from django.db import models

class City(models.Model):
    name = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    province = models.CharField(max_length=40, default="")

    class Meta:
        db_table = 'cities'


class Dataset(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    BPS_poverty_rate = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    sum_price_car = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    avg_price_car = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    std_price_car = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    sum_sold_car = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    avg_sold_car = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    std_sold_car = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    sum_viewer_car = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    avg_viewer_car = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    std_viewer_car = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    sum_buyer_car = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    avg_buyer_car = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    std_buyer_car = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    sum_price_motor = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    avg_price_motor = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    std_price_motor = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    sum_sold_motor = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    avg_sold_motor = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    std_sold_motor = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    sum_viewer_motor = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    avg_viewer_motor = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    std_viewer_motor = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    sum_buyer_motor = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    avg_buyer_motor = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    std_buyer_motor = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    sum_price_rumah_sell = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    avg_price_rumah_sell = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    std_price_rumah_sell = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    sum_sold_rumah_sell = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    avg_sold_rumah_sell = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    std_sold_rumah_sell = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    sum_viewer_rumah_sell = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    avg_viewer_rumah_sell = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    std_viewer_rumah_sell = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    sum_buyer_rumah_sell = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    avg_buyer_rumah_sell = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    std_buyer_rumah_sell = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    sum_price_rumah_rent = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    avg_price_rumah_rent = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    std_price_rumah_rent = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    sum_sold_rumah_rent = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    avg_sold_rumah_rent = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    std_sold_rumah_rent = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    sum_viewer_rumah_rent = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    avg_viewer_rumah_rent = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    std_viewer_rumah_rent = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    sum_buyer_rumah_rent = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    avg_buyer_rumah_rent = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    std_buyer_rumah_rent = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    sum_price_apt_sell = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    avg_price_apt_sell = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    std_price_apt_sell = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    sum_sold_apt_sell = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    avg_sold_apt_sell = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    std_sold_apt_sell = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    sum_viewer_apt_sell = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    avg_viewer_apt_sell = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    std_viewer_apt_sell = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    sum_buyer_apt_sell = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    avg_buyer_apt_sell = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    std_buyer_apt_sell = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    sum_price_apt_rent = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    avg_price_apt_rent = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    std_price_apt_rent = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    sum_sold_apt_rent = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    avg_sold_apt_rent = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    std_sold_apt_rent = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    sum_viewer_apt_rent = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    avg_viewer_apt_rent = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    std_viewer_apt_rent = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    sum_buyer_apt_rent = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    avg_buyer_apt_rent = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    std_buyer_apt_rent = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    sum_price_land_sell = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    avg_price_land_sell = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    std_price_land_sell = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    sum_sold_land_sell = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    avg_sold_land_sell = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    std_sold_land_sell = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    sum_viewer_land_sell = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    avg_viewer_land_sell = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    std_viewer_land_sell = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    sum_buyer_land_sell = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    avg_buyer_land_sell = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    std_buyer_land_sell = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    sum_price_land_rent = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    avg_price_land_rent = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    std_price_land_rent = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    sum_sold_land_rent = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    avg_sold_land_rent = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    std_sold_land_rent = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    sum_viewer_land_rent = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    avg_viewer_land_rent = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    std_viewer_land_rent = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    sum_buyer_land_rent = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    avg_buyer_land_rent = models.DecimalField(max_digits=25, decimal_places=7, default=0)
    std_buyer_land_rent = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        db_table = 'ecommerce_transactions'

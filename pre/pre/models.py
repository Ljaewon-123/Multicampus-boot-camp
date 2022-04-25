# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BuTempData(models.Model):
    obs_code = models.CharField(primary_key=True, max_length=20)
    record_time = models.TextField(blank=True, null=True)
    water_temp = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bu_temp_data'


class JoActualCondelData(models.Model):
    obs_code = models.CharField(primary_key=True, max_length=20)
    record_time = models.TextField(blank=True, null=True)
    wind_dir = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jo_actual_condel_data'


class JoActualWindData(models.Model):
    obs_code = models.CharField(primary_key=True, max_length=20)
    record_time = models.TextField(blank=True, null=True)
    wind_dir = models.TextField(blank=True, null=True)
    wind_speed = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jo_actual_wind_data'


class JoTempData(models.Model):
    obs_code = models.CharField(primary_key=True, max_length=20)
    record_time = models.TextField(blank=True, null=True)
    water_temp = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jo_temp_data'


class ObsList(models.Model):
    obs_code = models.CharField(primary_key=True, max_length=20)
    data_type = models.TextField(blank=True, null=True)
    obs_lat = models.TextField(blank=True, null=True)
    obs_lon = models.TextField(blank=True, null=True)
    obs_post_name = models.TextField(blank=True, null=True)
    obs_object = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'obs_list'


class Pago(models.Model):
    obs_code = models.CharField(primary_key=True, max_length=20)
    record_time = models.TextField(blank=True, null=True)
    wave_height = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pago'


class Tidalbuwind(models.Model):
    obs_code = models.CharField(primary_key=True, max_length=20)
    record_time = models.TextField(blank=True, null=True)
    wind_dir = models.TextField(blank=True, null=True)
    wind_speed = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tidalbuwind'

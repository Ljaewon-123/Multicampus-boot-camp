# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class InfCarAcc(models.Model):
    id = models.IntegerField(primary_key=True)
    cg = models.TextField(db_column='CG', blank=True, null=True)  # Field name made lowercase.
    sum = models.IntegerField(blank=True, null=True)
    ctop = models.IntegerField(db_column='CtoP', blank=True, null=True)  # Field name made lowercase.
    ctoc = models.IntegerField(db_column='CtoC', blank=True, null=True)  # Field name made lowercase.
    calone = models.IntegerField(db_column='CAlone', blank=True, null=True)  # Field name made lowercase.
    year_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inf_car_acc'


class InfChildZone(models.Model):
    id = models.IntegerField(primary_key=True)
    gugun = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    sname = models.TextField(blank=True, null=True)
    stype = models.TextField(blank=True, null=True)
    year_code = models.IntegerField(blank=True, null=True)
    sido = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inf_child_zone'


class InfEleDisplay(models.Model):
    id = models.IntegerField(primary_key=True)
    sido = models.TextField(blank=True, null=True)
    gugun = models.TextField(blank=True, null=True)
    year_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inf_ele_display'


class InfPopulation(models.Model):
    id = models.IntegerField(primary_key=True)
    year_code = models.IntegerField(blank=True, null=True)
    gugun = models.TextField(blank=True, null=True)
    household = models.IntegerField(blank=True, null=True)
    pop_sum = models.IntegerField(blank=True, null=True)
    male = models.IntegerField(blank=True, null=True)
    female = models.IntegerField(blank=True, null=True)
    sumkor = models.IntegerField(db_column='sumKor', blank=True, null=True)  # Field name made lowercase.
    korm = models.IntegerField(db_column='korM', blank=True, null=True)  # Field name made lowercase.
    korf = models.IntegerField(db_column='korF', blank=True, null=True)  # Field name made lowercase.
    sumfor = models.IntegerField(db_column='sumFor', blank=True, null=True)  # Field name made lowercase.
    form = models.IntegerField(db_column='forM', blank=True, null=True)  # Field name made lowercase.
    forf = models.IntegerField(db_column='forF', blank=True, null=True)  # Field name made lowercase.
    houseperperson = models.FloatField(db_column='HousePerPerson', blank=True, null=True)  # Field name made lowercase.
    over65 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inf_population'


class InfSmartCross(models.Model):
    id = models.IntegerField(primary_key=True)
    year_code = models.IntegerField(blank=True, null=True)
    sido = models.TextField(blank=True, null=True)
    gugun = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inf_smart_cross'


class InfSmartLamp(models.Model):
    id = models.IntegerField(primary_key=True)
    gugun = models.TextField(blank=True, null=True)
    data_date = models.TextField(blank=True, null=True)
    sido = models.TextField(blank=True, null=True)
    year_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inf_smart_lamp'


class InfSpeedBump(models.Model):
    id = models.IntegerField(primary_key=True)
    sido = models.TextField(blank=True, null=True)
    gugun = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    year_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inf_speed_bump'


class InfUnCamera(models.Model):
    id = models.IntegerField(primary_key=True)
    sido = models.TextField(blank=True, null=True)
    gugun = models.TextField(blank=True, null=True)
    gubun = models.IntegerField(blank=True, null=True)
    type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    year_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inf_un_camera'


class InfYellowcarpet(models.Model):
    id = models.IntegerField(primary_key=True)
    address = models.TextField(blank=True, null=True)
    year_code = models.IntegerField(blank=True, null=True)
    sido = models.TextField(blank=True, null=True)
    gugun = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inf_yellowcarpet'


class Year(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'year'

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountEmailaddress(models.Model):
    email = models.CharField(unique=True, max_length=254)
    verified = models.IntegerField()
    primary = models.IntegerField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BuTempData(models.Model):
    obs_code = models.CharField(primary_key=True, max_length=20)
    record_time = models.TextField(blank=True, null=True)
    water_temp = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bu_temp_data'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


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


class Mymember(models.Model):
    myname = models.CharField(primary_key=True,max_length=100, db_collation='utf8mb4_bin')
    mypassword = models.TextField(blank=True, null=True)
    myemail = models.TextField(blank=True, null=True)
    plaice = models.IntegerField(blank=True, null=True)             # 넙치, 광어
    rockfish = models.IntegerField(blank=True, null=True)           # 조피볼락 ,우럭
    schlegelii = models.IntegerField(blank=True, null=True)         # 감성돔
    striped_beakfish = models.IntegerField(blank=True, null=True)   # 돌돔
    pagrus_major = models.IntegerField(blank=True, null=True)       # 참돔
    length = models.TextField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mymember'


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


class SocialaccountSocialaccount(models.Model):
    provider = models.CharField(max_length=30)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    extra_data = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)
    key = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialappSites(models.Model):
    id = models.BigAutoField(primary_key=True)
    socialapp = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp_sites'
        unique_together = (('socialapp', 'site'),)


class SocialaccountSocialtoken(models.Model):
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)


class Tidalbuwind(models.Model):
    obs_code = models.CharField(primary_key=True, max_length=20)
    record_time = models.TextField(blank=True, null=True)
    wind_dir = models.TextField(blank=True, null=True)
    wind_speed = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tidalbuwind'

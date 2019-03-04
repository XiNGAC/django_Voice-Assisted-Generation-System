# database version: 5.7.21
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CmdbUserinfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'cmdb_userinfo'


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


class Patient(models.Model):
    patient_id = models.CharField(primary_key=True, max_length=255)
    patient_name = models.CharField(max_length=20)
    patient_sex = models.IntegerField()
    patient_age = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'patient'
        unique_together = (('patient_id', 'patient_name'),)


class ReportDetail(models.Model):
    report_id = models.CharField(primary_key=True, max_length=20)
    patient_id = models.CharField(max_length=255)
    department_name = models.CharField(max_length=255)
    check_item = models.CharField(max_length=255)
    machine_number = models.CharField(max_length=20)
    size_right_ul = models.FloatField(db_column='size_right_UL', blank=True, null=True)  # Field name made lowercase.
    size_right_lr = models.FloatField(db_column='size_right_LR', blank=True, null=True)  # Field name made lowercase.
    size_right_fb = models.FloatField(db_column='size_right_FB', blank=True, null=True)  # Field name made lowercase.
    size_left_ul = models.FloatField(db_column='size_left_UL', blank=True, null=True)  # Field name made lowercase.
    size_left_lr = models.FloatField(db_column='size_left_LR', blank=True, null=True)  # Field name made lowercase.
    size_left_fb = models.FloatField(db_column='size_left_FB', blank=True, null=True)  # Field name made lowercase.
    size_thickness = models.FloatField(blank=True, null=True)
    size_normal = models.CharField(max_length=255, blank=True, null=True)
    envelope = models.CharField(max_length=255, blank=True, null=True)
    substantial_echo = models.CharField(max_length=255, blank=True, null=True)
    lump_echo = models.CharField(max_length=255, blank=True, null=True)
    blood_flow_distribution = models.CharField(max_length=255, blank=True, null=True)
    blood_flow_spectrum = models.CharField(max_length=255, blank=True, null=True)
    left_psv = models.FloatField(db_column='left_PSV', blank=True, null=True)  # Field name made lowercase.
    left_edv = models.FloatField(db_column='left_EDV', blank=True, null=True)  # Field name made lowercase.
    right_psv = models.FloatField(db_column='right_PSV', blank=True, null=True)  # Field name made lowercase.
    right_edv = models.FloatField(db_column='right_EDV', blank=True, null=True)  # Field name made lowercase.
    diagnosis = models.CharField(max_length=255, blank=True, null=True)
    review_physician = models.CharField(max_length=255, blank=True, null=True)
    check_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_detail'

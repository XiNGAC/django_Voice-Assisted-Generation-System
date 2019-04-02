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


class ChangeInfo(models.Model):
    change_id = models.AutoField(primary_key=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    num = models.CharField(max_length=255, blank=True, null=True)
    size = models.CharField(max_length=255, blank=True, null=True)
    grow = models.CharField(max_length=255, blank=True, null=True)
    shape = models.CharField(max_length=255, blank=True, null=True)
    edge = models.CharField(max_length=255, blank=True, null=True)
    boundary = models.CharField(max_length=255, blank=True, null=True)
    echo_inside = models.CharField(max_length=255, blank=True, null=True)
    structure = models.CharField(max_length=255, blank=True, null=True)
    echo_back = models.CharField(max_length=255, blank=True, null=True)
    cdfi = models.CharField(max_length=255, blank=True, null=True)
    calcification = models.CharField(max_length=255, blank=True, null=True)
    echo_strong = models.CharField(max_length=255, blank=True, null=True)
    sound = models.CharField(max_length=255, blank=True, null=True)
    halo = models.CharField(max_length=255, blank=True, null=True)
    supplement = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'change_info'


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


class NormalInfo(models.Model):
    normal_id = models.AutoField(primary_key=True)
    size_fb = models.CharField(db_column='size_FB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    size_lr = models.CharField(db_column='size_LR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shape = models.CharField(max_length=255, blank=True, null=True)
    echo = models.CharField(max_length=255, blank=True, null=True)
    echo_division = models.CharField(max_length=255, blank=True, null=True)
    edge = models.CharField(max_length=255, blank=True, null=True)
    surface = models.CharField(max_length=255, blank=True, null=True)
    envelope = models.CharField(max_length=255, blank=True, null=True)
    cdfi = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'normal_info'


class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True, max_length=255)
    patient_name = models.CharField(max_length=20)
    patient_sex = models.IntegerField()
    patient_age = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'patient'
        unique_together = (('patient_id', 'patient_name'),)


class ReportDetail(models.Model):
    report_id = models.AutoField(primary_key=True)
    patient_id = models.CharField(max_length=255)
    department_name = models.CharField(max_length=255)
    check_number = models.CharField(max_length=20, blank=True, null=True)
    clinic_number = models.CharField(max_length=20, blank=True, null=True)
    check_item = models.CharField(max_length=255)
    machine_number = models.CharField(max_length=20)
    size_thickness = models.CharField(max_length=255, blank=True, null=True)
    diagnosis = models.CharField(max_length=255, blank=True, null=True)
    review_physician = models.CharField(max_length=255, blank=True, null=True)
    check_date = models.DateField(blank=True, null=True)
    normal_right = models.ForeignKey(NormalInfo, models.DO_NOTHING, db_column='normal_right', blank=True, null=True, related_name='n_r')
    normal_left = models.ForeignKey(NormalInfo, models.DO_NOTHING, db_column='normal_left', blank=True, null=True, related_name='n_l')
    change_right = models.ForeignKey(ChangeInfo, models.DO_NOTHING, db_column='change_right', blank=True, null=True, related_name='c_r')
    change_left = models.ForeignKey(ChangeInfo, models.DO_NOTHING, db_column='change_left', blank=True, null=True, related_name='c_l')
    change_thickness = models.ForeignKey(ChangeInfo, models.DO_NOTHING, db_column='change_thickness', blank=True, null=True, related_name='c_t')

    class Meta:
        managed = False
        db_table = 'report_detail'

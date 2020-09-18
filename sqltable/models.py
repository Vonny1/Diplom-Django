# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.core import serializers
from django.http import JsonResponse


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

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


class Bankaccount(models.Model):
    bankaccount_id = models.AutoField(db_column='Bankaccount_id', primary_key=True)  # Field name made lowercase.
    worker = models.ForeignKey('Worker', models.DO_NOTHING, db_column='Worker_id', blank=True, null=True)  # Field name made lowercase.
    account = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bankaccount'


class Brigade(models.Model):
    brigade_id = models.AutoField(db_column='Brigade_id', primary_key=True)  # Field name made lowercase.
    department = models.ForeignKey('Department', models.DO_NOTHING, db_column='Department_id', blank=True, null=True)  # Field name made lowercase.
    brigadeleader = models.ForeignKey('Brigadeleader', models.DO_NOTHING, db_column='Brigadeleader_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'brigade'


class Brigadeleader(models.Model):
    brigadeleader_id = models.AutoField(db_column='Brigadeleader_id', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    patronym = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'brigadeleader'


class Brigadeworker(models.Model):
    brigadeworker_id = models.AutoField(db_column='Brigadeworker_id', primary_key=True)  # Field name made lowercase.
    brigade = models.ForeignKey(Brigade, models.DO_NOTHING, db_column='Brigade_id', blank=True, null=True)  # Field name made lowercase.
    worker = models.ForeignKey('Worker', models.DO_NOTHING, db_column='Worker_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'brigadeworker'


class Customer(models.Model):
    customer_id = models.AutoField(db_column='Customer_id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class Department(models.Model):
    department_id = models.AutoField(db_column='Department_id', primary_key=True)  # Field name made lowercase.
    department = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'


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


class Ordercustomer(models.Model):
    ordercustomer_id = models.AutoField(db_column='Ordercustomer_id', primary_key=True)  # Field name made lowercase.
    orderproduct = models.ForeignKey('Orderproduct', models.DO_NOTHING, db_column='Orderproduct_id', blank=True, null=True)  # Field name made lowercase.
    customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='Customer_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ordercustomer'


class Orderproduct(models.Model):
    orderproduct_id = models.AutoField(db_column='Orderproduct_id', primary_key=True)  # Field name made lowercase.
    date = models.DateTimeField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING, db_column='Product_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orderproduct'


class Premium(models.Model):
    premium_id = models.AutoField(db_column='Premium_id', primary_key=True)  # Field name made lowercase.
    worker = models.ForeignKey('Worker', models.DO_NOTHING, db_column='Worker_id', blank=True, null=True)  # Field name made lowercase.
    premium = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'premium'


class Premiumbudget(models.Model):
    premiumbudget_id = models.AutoField(db_column='Premiumbudget_id', primary_key=True)  # Field name made lowercase.
    month = models.CharField(max_length=255, blank=True, null=True)
    budget = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'premiumbudget'


class Product(models.Model):
    product_id = models.AutoField(db_column='Product_id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class Productionjournal(models.Model):
    productionjournal_id = models.AutoField(db_column='Productionjournal_id', primary_key=True)  # Field name made lowercase.
    brigadeworker = models.ForeignKey(Brigadeworker, models.DO_NOTHING, db_column='Brigadeworker_id', blank=True, null=True)  # Field name made lowercase.
    product = models.ForeignKey(Product, models.DO_NOTHING, db_column='Product_id', blank=True, null=True)  # Field name made lowercase.
    quantity = models.SmallIntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productionjournal'


class Productionplan(models.Model):
    productionplan_id = models.AutoField(db_column='Productionplan_id', primary_key=True)  # Field name made lowercase.
    brigadeworker = models.ForeignKey(Brigadeworker, models.DO_NOTHING, db_column='Brigadeworker_id', blank=True, null=True)  # Field name made lowercase.
    product = models.ForeignKey(Product, models.DO_NOTHING, db_column='Product_id', blank=True, null=True)  # Field name made lowercase.
    quantity = models.SmallIntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productionplan'


class Rack(models.Model):
    rack_id = models.AutoField(db_column='Rack_id', primary_key=True)  # Field name made lowercase.
    quantity = models.IntegerField(blank=True, null=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, db_column='Product_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rack'


class Rackfreesize(models.Model):
    rack = models.ForeignKey(Rack, models.DO_NOTHING, db_column='Rack_id', blank=True, null=True)  # Field name made lowercase.
    freesize = models.IntegerField(blank=True, null=True)
    rackfreesize_id = models.AutoField(db_column='Rackfreesize_id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rackfreesize'


class Rackoccupiedsize(models.Model):
    rack = models.ForeignKey(Rack, models.DO_NOTHING, db_column='Rack_id', blank=True, null=True)  # Field name made lowercase.
    occupiedsize = models.IntegerField(blank=True, null=True)
    rackoccupiedsize_id = models.AutoField(db_column='Rackoccupiedsize_id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rackoccupiedsize'


class Racksize(models.Model):
    rack = models.ForeignKey(Rack, models.DO_NOTHING, db_column='Rack_id', blank=True, null=True)  # Field name made lowercase.
    size = models.IntegerField(blank=True, null=True)
    racksize_id = models.AutoField(db_column='Racksize_id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'racksize'


class Vacationcalendar(models.Model):
    vacationcalendar_id = models.AutoField(db_column='Vacationcalendar_id', primary_key=True)  # Field name made lowercase.
    worker = models.ForeignKey('Worker', models.DO_NOTHING, db_column='Worker_id', blank=True, null=True)  # Field name made lowercase.
    firstdate = models.DateField(blank=True, null=True)
    lastdate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vacationcalendar'


class Wage(models.Model):
    wage_id = models.AutoField(db_column='Wage_id', primary_key=True)  # Field name made lowercase.
    worker = models.ForeignKey('Worker', models.DO_NOTHING, db_column='Worker_id', blank=True, null=True)  # Field name made lowercase.
    wage = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wage'


class Worker(models.Model):
    worker_id = models.AutoField(db_column='Worker_id', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    patronymic = models.CharField(max_length=255, blank=True, null=True)
#    def obj_to_str(self):
#        return " {} {} {} {}  ".format(self.worker_id,self.firstname, self.lastname,self.patronymic)

    class Meta:
        managed = False
        db_table = 'worker'
        unique_together = (('worker_id', 'firstname', 'lastname', 'patronymic'),)

class Workerexperience(models.Model):
    workerexperience_id = models.AutoField(db_column='Workerexperience_id', primary_key=True)  # Field name made lowercase.
    worker = models.ForeignKey(Worker, models.DO_NOTHING, db_column='Worker_id', blank=True, null=True)  # Field name made lowercase.
    firstdate = models.DateField(blank=True, null=True)
    expdate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workerexperience'


class Workerfullinfo(models.Model):
    worker = models.ForeignKey(Worker, models.DO_NOTHING, db_column='Worker_id')  # Field name made lowercase.
    address = models.CharField(max_length=255, blank=True, null=True)
    phonenumber = models.IntegerField(blank=True, null=True)
    workerfullinfo_id = models.AutoField(db_column='Workerfullinfo_id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'workerfullinfo'

class Workerarrive(models.Model):
    workerarrive_id = models.AutoField(db_column='Workerarrive_id', primary_key=True)  # Field name made lowercase.
    worker = models.ForeignKey(Worker, models.DO_NOTHING, db_column='Worker_id', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workerarrive'

class Workerdepart(models.Model):
    workerdepart_id = models.AutoField(db_column='Workerdepart_id', primary_key=True)  # Field name made lowercase.
    time = models.TimeField(blank=True, null=True)
    workerarrive = models.ForeignKey(Workerarrive, models.DO_NOTHING, db_column='Workerarrive_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'workerdepart'


class Workerefftime(models.Model):
    workerefftime_id = models.AutoField(db_column='Workerefftime_id', primary_key=True)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    efftime = models.TimeField(blank=True, null=True)
    worker = models.ForeignKey(Worker, models.DO_NOTHING, db_column='Worker_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'workerefftime'


WorkerResponse = serializers.serialize("json", Worker.objects.all())
WorkerfullinfoResponse  = serializers.serialize("json", Workerfullinfo.objects.all())
jsontext = serializers.serialize("json", Workerdepart.objects.all())






































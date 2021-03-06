# Generated by Django 3.0.7 on 2020-06-18 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqltable', '0002_workerarrive'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workerdepart',
            fields=[
                ('workerdepart_id', models.AutoField(db_column='Workerdepart_id', primary_key=True, serialize=False)),
                ('time', models.TimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'workerdepart',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Workerefftime',
            fields=[
                ('workerefftime_id', models.AutoField(db_column='Workerefftime_id', primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True, null=True)),
                ('efftime', models.TimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'workerefftime',
                'managed': False,
            },
        ),
    ]

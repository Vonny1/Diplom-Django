# Generated by Django 3.0.7 on 2020-06-18 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqltable', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workerarrive',
            fields=[
                ('workerarrive_id', models.AutoField(db_column='Workerarrive_id', primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'workerarrive',
                'managed': False,
            },
        ),
    ]
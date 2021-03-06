# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-04 11:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CSVFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(default='File_path', max_length=128)),
                ('file', models.FileField(default='Server_path', upload_to='files/')),
                ('creation_date', models.DateTimeField(auto_now=True)),
                ('my_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CSVModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now=True)),
                ('field_1', models.CharField(max_length=100)),
                ('field_2', models.CharField(max_length=100)),
                ('field_3', models.CharField(max_length=100)),
                ('field_4', models.CharField(max_length=100)),
                ('field_5', models.CharField(max_length=100)),
                ('field_6', models.CharField(max_length=100)),
                ('field_7', models.CharField(max_length=100)),
                ('field_8', models.CharField(max_length=100)),
                ('field_9', models.CharField(max_length=100)),
                ('field_10', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

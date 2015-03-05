# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=1000)),
                ('created_on', models.DateField()),
                ('expires_on', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AdvertisementCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AdvertisementPhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('content', models.BinaryField(verbose_name=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='category',
            field=models.ForeignKey(to='advertisement.AdvertisementCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='advertisement',
            name='client',
            field=models.ForeignKey(to='client.Client'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='advertisement',
            name='photo',
            field=models.ForeignKey(to='advertisement.AdvertisementPhoto'),
            preserve_default=True,
        ),
    ]

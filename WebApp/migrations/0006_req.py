# Generated by Django 3.0.8 on 2020-11-21 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0005_auto_20201121_1334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Req',
            fields=[
                ('req_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=64)),
                ('symptoms', models.TextField()),
                ('emg_phone', models.CharField(max_length=64)),
            ],
        ),
    ]

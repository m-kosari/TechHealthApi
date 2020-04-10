# Generated by Django 3.0.5 on 2020-04-10 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Info', '0002_auto_20200409_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pck', models.CharField(max_length=200)),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Statuses',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('id_user', models.IntegerField()),
                ('pck', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('date', models.CharField(max_length=15)),
                ('long', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id_user', models.IntegerField()),
                ('dev_id', models.CharField(max_length=200)),
                ('dev_name', models.CharField(max_length=120)),
                ('dev_model', models.CharField(max_length=120)),
            ],
        ),
    ]

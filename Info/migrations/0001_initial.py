# Generated by Django 3.0.5 on 2020-04-07 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=200)),
                ('g_id', models.CharField(max_length=60)),
                ('name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=5)),
            ],
        ),
    ]

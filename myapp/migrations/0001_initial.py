# Generated by Django 2.1.1 on 2018-10-09 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=52)),
                ('name', models.CharField(max_length=15)),
                ('school', models.CharField(max_length=50)),
                ('Department', models.CharField(max_length=10)),
                ('sport', models.CharField(max_length=10)),
                ('cellphone', models.CharField(max_length=10)),
            ],
        ),
    ]
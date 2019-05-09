# Generated by Django 2.1.1 on 2018-11-21 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_team_upload_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='is_check',
            field=models.IntegerField(default=0, verbose_name='是否資料確認'),
        ),
        migrations.AlterField(
            model_name='team',
            name='upload_paid',
            field=models.ImageField(blank=True, default=None, upload_to='img/', verbose_name='是否上傳付費照'),
        ),
    ]
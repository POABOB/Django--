# Generated by Django 2.1.1 on 2018-11-11 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20181108_0020'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-publish',), 'verbose_name': '公告', 'verbose_name_plural': '公告'},
        ),
        migrations.AlterModelOptions(
            name='realteammember',
            options={'verbose_name': '隊伍成員(已審核)', 'verbose_name_plural': '隊伍成員(已審核)'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name': '隊伍', 'verbose_name_plural': '隊伍'},
        ),
        migrations.AlterModelOptions(
            name='teammember',
            options={'verbose_name': '隊伍成員(未審核)', 'verbose_name_plural': '隊伍成員(未審核)'},
        ),
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name': '會員資訊', 'verbose_name_plural': '會員資訊'},
        ),
        migrations.AlterField(
            model_name='realteammember',
            name='TeamName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Team', verbose_name='隊伍名稱'),
        ),
        migrations.AlterField(
            model_name='realteammember',
            name='birthday',
            field=models.CharField(max_length=10, verbose_name='生日'),
        ),
        migrations.AlterField(
            model_name='realteammember',
            name='cellphone',
            field=models.CharField(max_length=10, verbose_name='手機'),
        ),
        migrations.AlterField(
            model_name='realteammember',
            name='id_number',
            field=models.CharField(max_length=10, verbose_name='身分證'),
        ),
        migrations.AlterField(
            model_name='realteammember',
            name='is_PE',
            field=models.IntegerField(default=0, verbose_name='體保'),
        ),
        migrations.AlterField(
            model_name='realteammember',
            name='is_foreign',
            field=models.IntegerField(default=0, verbose_name='外籍'),
        ),
        migrations.AlterField(
            model_name='realteammember',
            name='member',
            field=models.CharField(max_length=40, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='realteammember',
            name='position',
            field=models.CharField(max_length=5, verbose_name='身分'),
        ),
        migrations.AlterField(
            model_name='realteammember',
            name='std_id',
            field=models.CharField(max_length=20, verbose_name='學號'),
        ),
        migrations.AlterField(
            model_name='team',
            name='TeamName',
            field=models.CharField(max_length=10, unique=True, verbose_name='隊伍名稱'),
        ),
        migrations.AlterField(
            model_name='team',
            name='email',
            field=models.EmailField(default='', max_length=50, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='team',
            name='is_active',
            field=models.IntegerField(default=0, verbose_name='是否提交隊員資料'),
        ),
        migrations.AlterField(
            model_name='team',
            name='is_paid',
            field=models.IntegerField(default=0, verbose_name='是否付費'),
        ),
        migrations.AlterField(
            model_name='team',
            name='is_pass',
            field=models.IntegerField(default=0, verbose_name='是否審核'),
        ),
        migrations.AlterField(
            model_name='team',
            name='memberNum',
            field=models.IntegerField(default=0, verbose_name='隊員人數'),
        ),
        migrations.AlterField(
            model_name='team',
            name='not_active',
            field=models.IntegerField(default=1, verbose_name='是否提交隊名'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='TeamName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Team', verbose_name='隊伍名稱'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='birthday',
            field=models.CharField(max_length=10, verbose_name='生日'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='cellphone',
            field=models.CharField(max_length=10, verbose_name='手機'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='id_number',
            field=models.CharField(max_length=10, verbose_name='身分證'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='is_PE',
            field=models.IntegerField(default=0, verbose_name='體保'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='is_foreign',
            field=models.IntegerField(default=0, verbose_name='外籍'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='member',
            field=models.CharField(max_length=40, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='position',
            field=models.CharField(max_length=5, verbose_name='身分'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='std_id',
            field=models.CharField(max_length=20, verbose_name='學號'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='cellphone',
            field=models.CharField(max_length=10, verbose_name='手機'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='department',
            field=models.CharField(max_length=10, verbose_name='科系'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.CharField(max_length=50, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='last_login',
            field=models.DateTimeField(auto_now=True, verbose_name='上次登入時間'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='name',
            field=models.CharField(max_length=15, verbose_name='名字'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='password',
            field=models.CharField(max_length=52, verbose_name='密碼'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='school',
            field=models.CharField(max_length=50, verbose_name='學校'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='status',
            field=models.BigIntegerField(default=0, verbose_name='狀態'),
        ),
    ]

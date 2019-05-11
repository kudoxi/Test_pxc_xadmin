# Generated by Django 2.2.1 on 2019-05-10 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_brand', models.ImageField(default='normal.png', upload_to='static/brand', verbose_name='logo标志')),
                ('btitle', models.CharField(max_length=64, verbose_name='名称')),
                ('isDelete', models.BooleanField(default=False, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '汽车品牌列表',
                'verbose_name_plural': '汽车品牌',
            },
        ),
        migrations.CreateModel(
            name='CarInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctitle', models.CharField(max_length=64, verbose_name='车名')),
                ('register_date', models.DateField(verbose_name='上牌日期')),
                ('engineNo', models.CharField(max_length=64, verbose_name='发动机号')),
                ('mileage', models.IntegerField(verbose_name='公里数')),
                ('maintenance', models.BooleanField(default=False, verbose_name='是否维修')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='价格')),
                ('extractprice', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='成交价格')),
                ('newprice', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='新车价格')),
                ('picture', models.ImageField(default='normal.png', upload_to='static/carinfo', verbose_name='图片')),
                ('formalities', models.BooleanField(default=False, verbose_name='是否办好手续')),
                ('debt', models.BooleanField(default=False, verbose_name='是否有债务')),
                ('promise', models.TextField(verbose_name='承诺')),
                ('examine', models.IntegerField(choices=[(0, '审核中'), (1, '审核通过'), (2, '审核未通过')], default=0, verbose_name='审核进度')),
                ('isPurchase', models.BooleanField(default=False, verbose_name='是否已出售')),
                ('isDeleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.Brand', verbose_name='品牌')),
            ],
            options={
                'verbose_name': '车辆信息列表',
                'verbose_name_plural': '车辆信息',
            },
        ),
    ]
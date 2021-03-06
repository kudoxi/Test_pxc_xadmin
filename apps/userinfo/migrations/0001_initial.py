# Generated by Django 2.2.1 on 2019-05-10 01:45

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.IntegerField(choices=[(0, '卖家'), (1, '买家')], default=0, verbose_name='角色')),
                ('isActive', models.BooleanField(default=True, verbose_name='是否激活')),
                ('isBan', models.BooleanField(default=False, verbose_name='是否禁用')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='消息内容')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='时间')),
                ('isRead', models.BooleanField(default=False, verbose_name='是否已读')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '消息记录列表',
                'verbose_name_plural': '消息记录',
            },
        ),
        migrations.CreateModel(
            name='DetailInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realname', models.CharField(max_length=64, verbose_name='真实姓名')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('ads', models.TextField(verbose_name='地址')),
                ('identity', models.CharField(max_length=18, verbose_name='身份证')),
                ('sex', models.IntegerField(choices=[(0, '男'), (1, '女')], default=0, verbose_name='性别')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('cellphone', models.CharField(max_length=20, verbose_name='手机号')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户信息列表',
                'verbose_name_plural': '用户信息',
            },
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bankNo', models.CharField(max_length=64, verbose_name='卡号')),
                ('bank', models.IntegerField(choices=[(0, '未绑定'), (1, '中国建设银行'), (2, '中国农业银行'), (3, '招商银行'), (4, '中国银行')], default=0, verbose_name='银行')),
                ('bankpwd', models.CharField(max_length=200, verbose_name='交易密码')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '银行信息列表',
                'verbose_name_plural': '银行信息',
            },
        ),
    ]

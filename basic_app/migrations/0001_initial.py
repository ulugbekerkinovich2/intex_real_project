# Generated by Django 4.0.3 on 2022-04-05 03:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kansultatsi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_Klent', models.CharField(max_length=300)),
                ('telNumberKlent', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Karkas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('latestCost', models.CharField(max_length=200)),
                ('nowCost', models.CharField(max_length=200)),
                ('howMuch', models.CharField(max_length=200)),
                ('frame', models.CharField(max_length=200)),
                ('size', models.CharField(max_length=200)),
                ('deep', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Naduvnie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('latestCost', models.CharField(max_length=200)),
                ('nowCost', models.CharField(max_length=200)),
                ('howMuch', models.CharField(max_length=200)),
                ('frame', models.CharField(max_length=200)),
                ('size', models.CharField(max_length=200)),
                ('deep', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Zakaz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=200)),
                ('telNumber', models.CharField(max_length=200)),
                ('poolFrame', models.CharField(max_length=200)),
                ('money', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('date_joined', models.DateField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-28 19:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_code', models.CharField(max_length=2)),
                ('number', models.CharField(max_length=9)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=50)),
                ('last_four_digits', models.CharField(max_length=4)),
                ('exp_month', models.CharField(max_length=2)),
                ('exp_year', models.CharField(max_length=4)),
                ('holder_name', models.CharField(max_length=50)),
                ('holder_birth_date', models.DateField()),
                ('cpf', models.CharField(max_length=11)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=3)),
                ('complement', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=2)),
                ('country', models.CharField(max_length=3)),
                ('postal_code', models.CharField(max_length=8)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
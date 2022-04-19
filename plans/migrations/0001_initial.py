# Generated by Django 4.0.3 on 2022-04-13 15:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('card', models.TextField()),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('pagseguro_plan_id', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]
# Generated by Django 4.0.3 on 2022-05-24 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0002_remove_alertsubtheme_alert_alert_gov_entites_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alert',
            old_name='gov_entites',
            new_name='gov_entities',
        ),
        migrations.AlterField(
            model_name='alert',
            name='territory_id',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
    ]
# Generated by Django 4.0.3 on 2022-05-02 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0004_alter_plansubscriptionstatus_pagseguro_notification_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='plansubscriptionstatus',
            name='pagseguro_notification_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plansubscriptionstatus',
            name='pagseguro_data',
            field=models.CharField(choices=[('INITIATED', 'INITIATED'), ('PENDING', 'PENDING'), ('ACTIVE', 'ACTIVE'), ('PAYMENT_METHOD_CHANGE', 'PAYMENT_METHOD_CHANGE'), ('SUSPENDED', 'SUSPENDED'), ('CANCELLED', 'CANCELLED'), ('CANCELLED_BY_RECEIVER', 'CANCELLED_BY_RECEIVER'), ('CANCELLED_BY_SENDER', 'CANCELLED_BY_SENDER'), ('EXPIRED', 'EXPIRED')], max_length=25),
        ),
    ]

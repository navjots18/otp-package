# Generated by Django 2.2.5 on 2021-04-22 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp', '0002_auto_20210422_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpmodel',
            name='can_send_otp_after',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

# Generated by Django 4.2.16 on 2024-10-11 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_alter_booking_appointmentday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='service',
            field=models.IntegerField(choices=[(0, 'Wash and Blow-Dry'), (1, 'Claw Clipping'), (2, 'Coat Trim'), (3, 'Teeth Clean'), (4, 'Flea Treatment and Worming'), (5, 'Paw Ear and Skin Treatment'), (6, 'Therapy Bath')]),
        ),
    ]

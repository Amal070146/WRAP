# Generated by Django 4.0.4 on 2023-03-04 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wrap', '0007_alter_booking_address_alter_booking_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='avatar',
            field=models.ImageField(default=123456, upload_to='images/'),
            preserve_default=False,
        ),
    ]

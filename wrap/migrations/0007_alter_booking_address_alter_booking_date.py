# Generated by Django 4.0.4 on 2023-03-04 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wrap', '0006_alter_booking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='address',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(verbose_name='Y-m-d'),
        ),
    ]
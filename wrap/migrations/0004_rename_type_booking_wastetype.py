# Generated by Django 4.0.4 on 2023-03-04 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wrap', '0003_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='type',
            new_name='wastetype',
        ),
    ]

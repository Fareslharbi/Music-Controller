# Generated by Django 4.1.7 on 2023-02-28 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='guest_can_skip',
            new_name='guest_can_pause',
        ),
    ]

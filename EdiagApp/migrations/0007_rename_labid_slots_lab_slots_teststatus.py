# Generated by Django 4.1.3 on 2024-02-26 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EdiagApp', '0006_slots_tsetid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slots',
            old_name='labId',
            new_name='lab',
        ),
        migrations.AddField(
            model_name='slots',
            name='testStatus',
            field=models.IntegerField(default=0),
        ),
    ]

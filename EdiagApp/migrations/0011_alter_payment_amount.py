# Generated by Django 4.1.3 on 2024-03-12 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EdiagApp', '0010_remove_slots_test_bookings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.IntegerField(),
        ),
    ]

# Generated by Django 4.1.3 on 2024-02-26 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EdiagApp', '0004_userreg_health'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('report', models.CharField(max_length=200, null=True)),
                ('prescription', models.CharField(max_length=200, null=True)),
                ('labId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EdiagApp.labreg')),
                ('userId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='EdiagApp.userreg')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('status', models.CharField(default='Succesfull', max_length=20)),
                ('slotId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EdiagApp.slots')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EdiagApp.userreg')),
            ],
        ),
    ]
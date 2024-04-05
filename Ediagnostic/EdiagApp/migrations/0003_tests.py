# Generated by Django 4.1.3 on 2024-02-23 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EdiagApp', '0002_labreg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EdiagApp.labreg')),
            ],
        ),
    ]

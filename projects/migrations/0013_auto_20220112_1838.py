# Generated by Django 3.2.4 on 2022-01-12 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20220112_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='gender',
            field=models.CharField(default='PUR binding', max_length=2000),
        ),
        migrations.AlterField(
            model_name='project',
            name='is_vacinated',
            field=models.BooleanField(default=False),
        ),
    ]
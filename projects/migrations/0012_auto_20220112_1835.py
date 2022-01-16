# Generated by Django 3.2.4 on 2022-01-12 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_remove_project_breed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='demo_link',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
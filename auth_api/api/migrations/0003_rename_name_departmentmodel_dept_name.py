# Generated by Django 3.2.5 on 2022-11-23 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20221122_2020'),
    ]

    operations = [
        migrations.RenameField(
            model_name='departmentmodel',
            old_name='name',
            new_name='dept_name',
        ),
    ]

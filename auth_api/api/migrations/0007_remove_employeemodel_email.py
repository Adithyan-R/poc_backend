# Generated by Django 3.2.5 on 2022-11-28 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20221127_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeemodel',
            name='email',
        ),
    ]

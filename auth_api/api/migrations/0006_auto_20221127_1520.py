# Generated by Django 3.2.5 on 2022-11-27 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20221123_2240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeemodel',
            old_name='dept',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='employeemodel',
            old_name='role',
            new_name='designation',
        ),
        migrations.AddField(
            model_name='employeemodel',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
    ]

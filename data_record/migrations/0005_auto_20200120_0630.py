# Generated by Django 3.0.1 on 2020-01-20 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_record', '0004_auto_20200120_0615'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='project_name',
            new_name='project_namei',
        ),
    ]
